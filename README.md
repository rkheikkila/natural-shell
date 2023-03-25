# natural-shell (nash)
Natural language interface to Unix shell.

Nash is a CLI tool that takes a free form description of a task to be achieved in Unix shell and asks ChatGPT to propose a command to complete the task.

Outputs of ChatGPT are not always correct, so use the tool with caution. In any case, the tool can be used to learn new commands.

## Installation

Nash should work on Python versions 3.7 and greater. The only dependency is the [OpenAI Python library](https://github.com/openai/openai-python).

To install nash, clone the repository and run `pip install .` in the main directory.

To get started you need to set your OpenAI API key in the `OPENAI_API_KEY` environment variable.

## Usage

```
$ nash delete all ".log" files older than 1 month in the current directory
-------------------- COMMANDS --------------------

find . -name '*.log' -mtime +30 -exec rm {} \;

-------------------- EXPLANATION --------------------

find . searches for all files in the current directory and its subdirectories,
 -name '*.log' specifies the files with extension .log,
 -mtime +30 selects only those files that are older than 30 days,
 -exec rm {} \; executes the rm command to remove the selected files.

Execute? (y/n)
```
