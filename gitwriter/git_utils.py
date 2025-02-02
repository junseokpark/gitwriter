import subprocess
import sys
from gitwriter.environment import load_environment
from openai import OpenAI, APIConnectionError, AuthenticationError


def fetch_staged_git_changes():
    """Retrieve staged git changes using git diff."""
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
    """Generate commit message using either External or Local API based on environment configuration."""
    env = load_environment()

    if env['TYPE'].lower() == "external api":
        return generate_external_commit_message(env, diff_content)
    else:
        return generate_local_commit_message(env, diff_content)


def generate_external_commit_message(env, diff_content):
    """Handles commit message generation via external API."""
    try:
        client = OpenAI(api_key=env['API_KEY'])
        api_response = client.chat.completions.create(
            model=env['MODEL'],
            messages=[
                {"role": "system", "content": "You are an assistant that generates concise git commit messages."},
                {"role": "user", "content": f"Generate a Git commit message for the following changes:\n\n{diff_content}"},
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


def generate_local_commit_message(env, diff_content):
    """Placeholder for local API commit message generation logic."""
    # Implement your logic to interact with local API (e.g., llama3, deepseek1)
    print(f"Local API model {env['MODEL']} selected at {env['API_ADDRESS']}.")
    # For now, returning a mock response
    return f"Generated commit message using local API model {env['MODEL']} (mock)."