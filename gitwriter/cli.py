from .git_utils import fetch_staged_git_changes, create_commit_message_from_diff

def main():
    changes = fetch_staged_git_changes()
    if not changes:
        print("No staged changes found.")
        return

    commit_message = create_commit_message_from_diff(changes)
    print(f"Generated Commit Message: {commit_message}")
    # Optional: Automatically commit
    # subprocess.run(["git", "commit", "-m", commit_message])

if __name__ == "__main__":
    main()