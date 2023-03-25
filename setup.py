from setuptools import setup

setup(
    name="nash",
    version="0.1",
    author="Rasmus Heikkilä",
    description="Natural language interface to Unix shell",
    entry_points={"console_scripts": ["nash = nash:main"]},
    py_modules=["nash", "prompts"],
    requires=["openai"],
)
