import argparse
from gitwriter.environment import setup_environment, load_environment, test_environment, ensure_environment
from gitwriter.git_utils import fetch_staged_git_changes, create_commit_message_from_diff


def main():
    parser = argparse.ArgumentParser(description='GitWriter CLI')
    parser.add_argument('command', choices=['setup', 'env', 'test', 'run'], help='Command to execute')
    args = parser.parse_args()

    if args.command == 'setup':
        setup_environment()
    elif args.command == 'env':
        env = load_environment()
        print("Current Environment Setup:")
        for key, value in env.items():
            print(f"{key}: {value}")
    elif args.command == 'test':
        test_environment()
    elif args.command == 'run':
        ensure_environment()
        changes = fetch_staged_git_changes()
        if not changes:
            print("No staged changes found.")
            return

        commit_message = create_commit_message_from_diff(changes)
        print(f"Generated Commit Message: {commit_message}")


if __name__ == "__main__":
    main()