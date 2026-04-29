import subprocess
import datetime

def run_git(command):
    try:
        result = subprocess.run(command, check=True, text=True, shell=True, capture_output=True)
        print(f"✅ Done: {command}")
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ ERROR in [{command}]: {e.stderr}")
        return False, e.stderr

def auto_publish():
    print("🚀 Starting Nexo Shopping Auto-Publish...")

    # Step 1: Nayi files ko add karo
    run_git("git add .")
    
    # Check if there's actually anything new to commit
    success, status_output = run_git("git status --porcelain")
    
    if not status_output.strip():
        print("ℹ️ No new changes detected. Skipping publish.")
        return

    # Step 2: Aaj ki date aur time ke sath commit message banao
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f'git commit -m "Auto-updated deals on {current_time}"'
    
    if run_git(commit_msg)[0]:
        # Step 3: GitHub par bhej do!
        print("⏳ Pushing code to GitHub... Please wait.")
        if run_git("git push origin main")[0]: 
            print("🎉 BINGO! Code successfully GitHub (aur Vercel) par push ho gaya hai!")

if __name__ == "__main__":
    auto_publish()