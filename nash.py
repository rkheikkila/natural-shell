"""
Natural language interface to Unix shell, powered by ChatGPT.

Author: Rasmus Heikkilä, 2023
"""
from dataclasses import dataclass
import json
import os
import subprocess
import sys

import openai

from prompts import system_prompt, user_instruction

model = "gpt-3.5-turbo"


@dataclass
class CommandResponse:
    commands: list[str]
    explanation: str


def get_command(task: str) -> CommandResponse:
    """Query for shell command from ChatGPT."""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": task + user_instruction}
    ]

    api_response = openai.ChatCompletion.create(
        model = model,
        messages = messages
    )

    assistant_response = json.loads(api_response["choices"][0]["message"]["content"])
    response = CommandResponse(**assistant_response)
    return response
    
    

def make_heading(heading: str, padding=20) -> str:
    dashes = "-" * padding
    return dashes + " " + heading + " " + dashes


def print_output(output: CommandResponse) -> None:
    print(make_heading("COMMANDS"))
    print("")

    for cmd in output.commands:
        print(cmd)
    
    print("")
    print(make_heading("EXPLANATION"))
    print("")
    print(output.explanation)
    print("")
    sys.stdout.flush()


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("A prompt is needed.")
        sys.exit(0)
    user_prompt = ' '.join(args)

    try:
        output = get_command(user_prompt)
    except Exception as e:
        print(f"Something went wrong: {str(e)}")
        sys.exit(1)

    print_output(output)
    user_response = input("Execute? (y/n) ")

    if user_response.strip().lower() not in ("y", "yes"):
        return

    for cmd in output.commands:
        result = subprocess.run(cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)
        if result.returncode:
            print("Command resulted in error, aborting.")
            break


if __name__ == "__main__":
    main()
