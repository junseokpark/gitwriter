# GitWriter

GitWriter is a command-line tool that uses OpenAI's API to generate helpful and concise commit messages based on your staged git changes.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

The GitWriter CLI provides the following commands:

`setup`: Set up the environment.

`env`: Load and display the current environment setup.

`test`: Test the environment.

`run`: Ensure the environment is set up and fetch staged Git changes.

## Commands

1) Set up the environment:

```bash
python cli.py setup
```

2) Load and display the current environment setup:

```bash
python cli.py env
```

3) Test the environment:

```bash
python cli.py test
```

4) Run the gitwriter:

```bash
python cli.py run
```

If there are no staged changes, GitWriter will print "No staged changes found."

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

© 2025 Junseok Park and Danielle Denisko. All rights reserved.

## References
https://dev.to/pranavraut033/automate-your-git-commit-messages-with-chatgpt-2dbk 