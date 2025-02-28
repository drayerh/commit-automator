# Commit Automator

Commit Automator is a Python script designed to automate the process of generating pseudo-random Python code, committing it to a local Git repository, and pushing the changes to a remote GitHub repository. This can be useful for testing, generating activity on a repository, or automating repetitive commit tasks.

## Features

- Generates realistic-looking Python code with random patterns.
- Creates and amends commits in a local Git repository.
- Pushes changes to a specified branch on a remote GitHub repository.

## Requirements

- Python 3.x
- `gitpython` library
- `faker` library
- `pytz` library

## Installation

1. Clone the repository:
    ```sh
    git clone git@github.com:drayerh/commit-automator.git
    cd commit-automator
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Edit the `main.py` file to configure the following settings:

- `REPO_PATH`: Local directory path for the repository.
- `GITHUB_URL`: SSH URL of the remote GitHub repository.
- `FILE_PATH`: Template for the generated code file names.
- `BRANCH_NAME`: Branch to push changes to.

## Usage

Run the script to generate code, create commits, and push changes:

```sh
python main.py