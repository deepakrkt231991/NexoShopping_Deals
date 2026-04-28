
import subprocess
import datetime

def auto_publish():
    """
    Automatically stages changes in index.html, creates a commit message
    with today's date, and pushes the changes to the remote GitHub repository.
    Includes error handling for Git commands.
    """
    today = datetime.date.today().strftime("%Y-%m-%d")
    commit_message = f"Auto-updated deals on {today}"

    try:
        # Stage changes in index.html
        add_result = subprocess.run(["git", "add", "."], check=True, capture_output=True, text=True)
        print(f"Staged changes: {add_result.stdout.strip()}")

        commit_result = subprocess.run(["git", "commit", "-m", commit_message], check=True, capture_output=True, text=True)
        print(f"Created commit: {commit_result.stdout.strip()}")

        push_result = subprocess.run(["git", "push", "origin", "main"], check=True, capture_output=True, text=True)
        print(f"Pushed changes: {push_result.stdout.strip()}")

    except subprocess.CalledProcessError as e:
        print(f"Error executing Git command: {e.cmd} - {e.stderr.strip()}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    auto_publish()
