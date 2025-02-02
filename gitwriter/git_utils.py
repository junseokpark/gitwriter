import subprocess
from openai import OpenAI, APIConnectionError, AuthenticationError
import os
import sys

def initialize_openai_client():
    """Initialize OpenAI client with error handling."""
    try:
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise EnvironmentError("OPENAI_API_KEY environment variable is not set.")
        return OpenAI(api_key=openai_api_key)
    except EnvironmentError as env_err:
        print(f"Environment Error: {env_err}")
        sys.exit(1)
    except Exception as err:
        print(f"Unexpected error initializing OpenAI client: {err}")
        sys.exit(1)

openai_client = initialize_openai_client()

def fetch_staged_git_changes():
    """Retrieve staged git changes."""
    try:
        git_process = subprocess.run(
            ["git", "diff", "--staged"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        if git_process.returncode != 0:
            raise subprocess.SubprocessError(git_process.stderr.strip())
        return git_process.stdout
    except subprocess.SubprocessError as git_err:
        print(f"Git Error: {git_err}")
        sys.exit(1)
    except Exception as err:
        print(f"Unexpected error retrieving git changes: {err}")
        sys.exit(1)

def create_commit_message_from_diff(diff_content):
    """Generate commit message using OpenAI API based on git diff."""
    try:
        api_response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant that generates helpful and concise git commit messages.",
                },
                {
                    "role": "user",
                    "content": f"Generate a Git commit message for the following changes, adhering to Git commit standards:\n\n{diff_content}",
                },
            ],
            max_tokens=350,
            temperature=0.5,
        )
        return api_response.choices[0].message.content.strip()
    except AuthenticationError as auth_err:
        print(f"Authentication Error: {auth_err}")
        sys.exit(1)
    except APIConnectionError as conn_err:
        print(f"API Connection Error: {conn_err}")
        sys.exit(1)
    except Exception as err:
        print(f"Unexpected error communicating with OpenAI API: {err}")
        sys.exit(1)