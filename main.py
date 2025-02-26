#!/usr/bin/env python3
import os
import random
from datetime import datetime, timedelta
from git import Repo, Actor
from faker import Faker
import pytz

# Configuration
REPO_PATH = '/home/drayerh/commit-automator'
GITHUB_URL = 'https://github.com/drayerh/commit-automator.git'
FILE_PATH = 'code_gen/code_{date}.py'
COMMIT_TIMES = 3  # Commits per run
DAYS_BACK = 365  # Spread commits over X days

# Initialize tools
fake = Faker()
actor = Actor("Commit Bot", "bot@example.com")


def generate_pseudo_code():
    """Generate realistic-looking Python code with random patterns"""
    code = []
    for _ in range(random.randint(5, 15)):
        var_name = fake.word().lower() + '_' + fake.word().lower()
        operation = random.choice(['+', '-', '*', '/'])
        value = random.randint(1, 100)
        code.append(f"{var_name} = {value} {operation} {random.randint(1, 100)}")

    code.append(f"def {fake.word()}_function():")
    code.append(f"    return {' + '.join([fake.word() for _ in range(3)])}")
    return '\n'.join(code)


def create_commit(repo, days_ago):
    commit_date = datetime.now(pytz.utc) - timedelta(days=days_ago)
    commit_date = commit_date.replace(hour=random.randint(9, 18),
                                      minute=random.randint(0, 59))

    # Generate file content
    file_name = FILE_PATH.format(date=commit_date.strftime("%Y%m%d_%H%M"))
    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    with open(file_name, 'w') as f:
        f.write(f"# Auto-generated at {commit_date.isoformat()}\n")
        f.write(generate_pseudo_code())

    # Add to index
    repo.index.add([file_name])

    # Create commit
    repo.index.commit(
        message=f"Add {os.path.basename(file_name)}",
        author=actor,
        committer=actor,
        author_date=commit_date.isoformat(),
        commit_date=commit_date.isoformat()
    )


def main():
    # Initialize repository
    if not os.path.exists(REPO_PATH):
        repo = Repo.clone_from(GITHUB_URL, REPO_PATH)
    else:
        repo = Repo(REPO_PATH)

    # Create multiple commits
    for _ in range(COMMIT_TIMES):
        try:
            days_ago = random.randint(1, DAYS_BACK)
            create_commit(repo, days_ago)
        except Exception as e:
            print(f"Error creating commit: {str(e)}")

    # Push changes
    try:
        origin = repo.remote(name='origin')
        origin.push()
        print("Successfully pushed changes")
    except Exception as e:
        print(f"Error pushing changes: {str(e)}")


if __name__ == "__main__":
    main()