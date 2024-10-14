## Table of Contents
1. [GitHub](#github)
2. [GitHub Workflow](#github-workflow)
   - [Initial Setup](#initial-setup)
   - [Working on Your Project](#working-on-your-project)
   - [Collaborating with Others](#collaborating-with-others)
   - [Keeping Your Fork Updated](#keeping-your-fork-updated)
   - [Final Steps](#final-steps)
   - [Summary of Commands](#summary-of-commands)

## GitHub

1. Make changes in files, e.g write code
2. Stage changes:
   - git add . (staging all changes)
   - or git add app.py (if app.py has the changes we want to stage)
   - or press "+" in VS Code under "Source Control"
3. Commit changes (this goes to your local clone or fork of the repo):
   - git commit -m "comment about the staged changes"
   - or press "Commit" in VS Code under "Source Control", and write a comment
4. Push changes to GitHub repo:
   - git push origin main

## GitHub Workflow

### Initial Setup

1. **Initialize a New Git Repository**:
   - If you are starting a new project, initialize a new Git repository:
     git init

2. **Clone an Existing Repository**:
   - If you are working on an existing project, clone the repository to your local machine:
     git clone https://github.com/username/repository.git

3. **Fork a Repository**:
   - If you want to contribute to a project, fork the repository on GitHub and then clone your fork:
     - Go to the repository on GitHub and click the "Fork" button.
     - Clone your forked repository:
       git clone https://github.com/your-username/repository.git

### Working on Your Project

4. **Create a New Branch**:
   - Create a new branch for your feature or bug fix (this is separate from `origin/main`):
     git checkout -b feature-branch

5. **Make Changes**:
   - Edit your files and make the necessary changes.

6. **Stage Changes**:
   - Stage the changes you want to commit:
     git add .
     - or stage specific files:
     git add app.py
     - or press "+" in VS Code under "Source Control".

7. **Commit Changes**:
   - Commit the staged changes with a descriptive message:
     git commit -m "Your descriptive commit message"
     - or press "Commit" in VS Code under "Source Control", and write a comment.

8. **Push Changes to GitHub**:
   - Push your branch to the remote repository:
     git push origin feature-branch

### Collaborating with Others

9. **Create a Pull Request**:
   - Go to your repository on GitHub.
   - Click the "Compare & pull request" button.
   - Create a pull request to merge your changes into the `main` branch.

10. **Review and Merge Pull Requests**:
    - Review pull requests from your team members.
    - Merge the pull requests after review and approval.

### Keeping Your Fork Updated

11. **Fetch and Merge Updates from the Original Repository**:
    - Add the original repository as a remote named `upstream`:
      git remote add upstream https://github.com/original-owner/repository.git
    - Fetch the latest changes from the original repository:
      git fetch upstream
    - Merge the changes into your local `main` branch:
      git checkout main
      git merge upstream/main

### Final Steps

12. **Switch Back to the Main Branch**:
    - After completing your feature or bug fix, switch back to the `main` branch:
      git checkout main

13. **Pull the Latest Changes**:
    - Pull the latest changes from the remote `main` branch:
      git pull origin main

14. **Delete the Feature Branch**:
    - After merging your feature branch, you can delete it:
      git branch -d feature-branch

### Summary of Commands
# Initialize a new Git repository
git init

# Clone an existing repository
git clone https://github.com/username/repository.git

# Create a new branch (separate from origin/main)
git checkout -b feature-branch

# Stage all changes
git add .

# Commit the changes
git commit -m "Your descriptive commit message"

# Push the branch to GitHub
git push origin feature-branch

# Add the original repository as a remote
git remote add upstream https://github.com/original-owner/repository.git

# Fetch and merge updates from the original repository
git fetch upstream
git checkout main
git merge upstream/main

# Pull the latest changes from the remote main branch
git pull origin main

# Delete the feature branch
git branch -d feature-branch