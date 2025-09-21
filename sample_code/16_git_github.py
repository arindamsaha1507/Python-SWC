# Episode 16: Git and GitHub Essentials for Scientists
# A comprehensive guide to version control for research code

import os
import subprocess
from datetime import datetime
from typing import List, Dict, Optional

print("🐙 Git and GitHub Essentials for Scientific Computing")
print("=" * 60)

# ============================================================
# Git Basics - Repository Setup and Configuration
# ============================================================

print("\n=== Git Repository Setup ===")

# Basic configuration commands (run these once on your system)
git_config_commands = [
    "# Configure your identity (required for commits)",
    "git config --global user.name 'Your Name'",
    "git config --global user.email 'your.email@university.edu'",
    "",
    "# Set default branch name",
    "git config --global init.defaultBranch main",
    "",
    "# Set default editor (optional)",
    "git config --global core.editor 'code --wait'  # VS Code",
    "git config --global core.editor 'nano'         # Nano editor",
    "",
    "# Improve output formatting",
    "git config --global color.ui auto",
    "git config --global core.autocrlf input  # Unix/Mac",
    "git config --global core.autocrlf true   # Windows",
    "",
    "# View current configuration",
    "git config --list",
    "git config user.name",
    "git config user.email",
]

print("📋 Essential Git Configuration:")
for cmd in git_config_commands:
    print(f"  {cmd}")

# Repository initialization
repo_setup_commands = [
    "# Create a new repository",
    "git init",
    "git init my-research-project",
    "",
    "# Clone an existing repository",
    "git clone https://github.com/username/repo-name.git",
    "git clone git@github.com:username/repo-name.git  # SSH",
    "",
    "# Clone to specific directory",
    "git clone https://github.com/username/repo-name.git my-local-name",
    "",
    "# Clone specific branch",
    "git clone -b branch-name https://github.com/username/repo-name.git",
]

print("\n📁 Repository Setup:")
for cmd in repo_setup_commands:
    print(f"  {cmd}")

# ============================================================
# Daily Git Workflow Commands
# ============================================================

print("\n=== Daily Git Workflow ===")

daily_workflow = [
    "# Check repository status",
    "git status",
    "git status -s  # Short format",
    "",
    "# Add files to staging area",
    "git add filename.py",
    "git add *.py                    # All Python files",
    "git add .                      # All files in current directory",
    "git add -A                     # All files in repository",
    "git add -u                     # Only tracked files",
    "",
    "# Remove files from staging",
    "git reset filename.py",
    "git reset                      # Remove all from staging",
    "",
    "# Commit changes",
    "git commit -m 'Add inflammation analysis function'",
    "git commit -am 'Fix bug in data loading'  # Add and commit tracked files",
    "",
    "# View commit history",
    "git log",
    "git log --oneline",
    "git log --graph --oneline --all",
    "git log --author='Your Name'",
    "git log --since='2 weeks ago'",
    "git log filename.py            # History of specific file",
]

print("📝 Daily Workflow Commands:")
for cmd in daily_workflow:
    print(f"  {cmd}")

# ============================================================
# Working with Files and Changes
# ============================================================

print("\n=== Working with Files and Changes ===")

file_operations = [
    "# View changes",
    "git diff                       # Unstaged changes",
    "git diff --staged              # Staged changes",
    "git diff HEAD~1                # Changes since last commit",
    "git diff branch-name           # Compare with another branch",
    "",
    "# Show specific commit",
    "git show HEAD",
    "git show commit-hash",
    "git show HEAD~2                # Two commits ago",
    "",
    "# Discard changes",
    "git checkout -- filename.py   # Discard unstaged changes",
    "git restore filename.py       # Modern syntax",
    "git restore --staged filename.py  # Unstage file",
    "",
    "# Remove files",
    "git rm filename.py             # Remove and stage deletion",
    "git rm --cached filename.py   # Remove from Git but keep file",
    "",
    "# Rename/move files",
    "git mv old-name.py new-name.py",
    "",
    "# Ignore files (.gitignore)",
    "echo '*.pyc' >> .gitignore",
    "echo '__pycache__/' >> .gitignore",
    "echo 'data/*.csv' >> .gitignore",
]

print("📄 File Operations:")
for cmd in file_operations:
    print(f"  {cmd}")

# ============================================================
# Branching and Merging
# ============================================================

print("\n=== Branching and Merging ===")

branching_commands = [
    "# List branches",
    "git branch                     # Local branches",
    "git branch -r                  # Remote branches",
    "git branch -a                  # All branches",
    "",
    "# Create branches",
    "git branch feature-analysis",
    "git checkout -b feature-plotting  # Create and switch",
    "git switch -c bugfix-data-loading  # Modern syntax",
    "",
    "# Switch branches",
    "git checkout main",
    "git switch feature-analysis   # Modern syntax",
    "",
    "# Merge branches",
    "git checkout main",
    "git merge feature-analysis",
    "",
    "# Delete branches",
    "git branch -d feature-analysis    # Safe delete",
    "git branch -D feature-analysis    # Force delete",
    "git push origin --delete feature-analysis  # Delete remote",
    "",
    "# Rebase (alternative to merge)",
    "git checkout feature-branch",
    "git rebase main",
    "",
    "# Interactive rebase (advanced)",
    "git rebase -i HEAD~3           # Last 3 commits",
]

print("🌿 Branching and Merging:")
for cmd in branching_commands:
    print(f"  {cmd}")

# ============================================================
# Working with Remote Repositories
# ============================================================

print("\n=== Remote Repository Operations ===")

remote_commands = [
    "# View remotes",
    "git remote -v",
    "",
    "# Add remote",
    "git remote add origin https://github.com/username/repo.git",
    "git remote add upstream https://github.com/original/repo.git",
    "",
    "# Fetch changes from remote",
    "git fetch origin",
    "git fetch --all",
    "",
    "# Pull changes (fetch + merge)",
    "git pull origin main",
    "git pull                       # From tracking branch",
    "git pull --rebase              # Rebase instead of merge",
    "",
    "# Push changes",
    "git push origin main",
    "git push origin feature-branch",
    "git push -u origin main        # Set upstream tracking",
    "git push --all                 # Push all branches",
    "git push --tags                # Push tags",
    "",
    "# Track remote branch",
    "git checkout -b local-branch origin/remote-branch",
    "git branch --set-upstream-to=origin/main main",
]

print("🌐 Remote Operations:")
for cmd in remote_commands:
    print(f"  {cmd}")

# ============================================================
# Tags and Releases
# ============================================================

print("\n=== Tags and Releases ===")

tagging_commands = [
    "# Create tags",
    "git tag v1.0.0",
    "git tag -a v1.0.0 -m 'Release version 1.0.0'",
    "git tag -a v1.0.1 commit-hash  # Tag specific commit",
    "",
    "# List tags",
    "git tag",
    "git tag -l 'v1.*'              # Pattern matching",
    "",
    "# Push tags",
    "git push origin v1.0.0",
    "git push origin --tags         # Push all tags",
    "",
    "# Delete tags",
    "git tag -d v1.0.0              # Delete local",
    "git push origin --delete v1.0.0  # Delete remote",
    "",
    "# Checkout tag",
    "git checkout v1.0.0",
    "git checkout -b hotfix-v1.0.1 v1.0.0",
]

print("🏷️ Tags and Releases:")
for cmd in tagging_commands:
    print(f"  {cmd}")

# ============================================================
# Undoing Changes and History Management
# ============================================================

print("\n=== Undoing Changes ===")

undo_commands = [
    "# Undo commits",
    "git reset --soft HEAD~1        # Undo commit, keep changes staged",
    "git reset HEAD~1               # Undo commit and staging",
    "git reset --hard HEAD~1        # Undo commit and changes (DANGEROUS)",
    "",
    "# Revert commits (safe for shared repos)",
    "git revert HEAD",
    "git revert commit-hash",
    "git revert HEAD~2..HEAD        # Revert range",
    "",
    "# Amend last commit",
    "git commit --amend -m 'New message'",
    "git add forgotten-file.py",
    "git commit --amend --no-edit",
    "",
    "# Cherry-pick commits",
    "git cherry-pick commit-hash",
    "git cherry-pick branch-name~2",
    "",
    "# Stash changes",
    "git stash",
    "git stash save 'Work in progress on analysis'",
    "git stash list",
    "git stash pop                  # Apply and remove",
    "git stash apply                # Apply but keep in stash",
    "git stash drop                 # Delete stash",
]

print("↩️ Undoing Changes:")
for cmd in undo_commands:
    print(f"  {cmd}")

# ============================================================
# GitHub-Specific Commands and Workflows
# ============================================================

print("\n=== GitHub-Specific Workflows ===")

github_workflows = [
    "# Fork workflow",
    "1. Fork repository on GitHub",
    "2. git clone https://github.com/YOUR-USERNAME/REPO-NAME.git",
    "3. git remote add upstream https://github.com/ORIGINAL-OWNER/REPO-NAME.git",
    "4. git fetch upstream",
    "5. git checkout main",
    "6. git merge upstream/main",
    "",
    "# Pull Request workflow",
    "1. git checkout -b feature-new-analysis",
    "2. # Make changes and commit",
    "3. git push origin feature-new-analysis",
    "4. # Create Pull Request on GitHub",
    "5. # After review and merge:",
    "6. git checkout main",
    "7. git pull upstream main",
    "8. git branch -d feature-new-analysis",
    "",
    "# GitHub CLI (gh) commands",
    "gh repo clone owner/repo",
    "gh repo fork owner/repo",
    "gh pr create --title 'Add new analysis' --body 'Description'",
    "gh pr list",
    "gh pr checkout 123",
    "gh pr merge 123",
    "gh issue create --title 'Bug report' --body 'Description'",
    "gh issue list",
]

print("🐱 GitHub Workflows:")
for cmd in github_workflows:
    print(f"  {cmd}")

# ============================================================
# Git Best Practices for Scientific Computing
# ============================================================

print("\n=== Git Best Practices for Scientists ===")

best_practices = [
    "📋 COMMIT MESSAGE GUIDELINES:",
    "  ✓ Use present tense: 'Add function' not 'Added function'",
    "  ✓ Keep first line under 50 characters",
    "  ✓ Be specific: 'Fix numpy array indexing bug' not 'Fix bug'",
    "  ✓ Reference issues: 'Fix data loading bug (fixes #123)'",
    "",
    "📁 REPOSITORY ORGANIZATION:",
    "  ✓ Use clear directory structure: data/, src/, tests/, docs/",
    "  ✓ Include README.md with setup instructions",
    "  ✓ Add LICENSE file for open science",
    "  ✓ Use .gitignore for generated files",
    "",
    "🔄 WORKFLOW RECOMMENDATIONS:",
    "  ✓ Commit often, push regularly",
    "  ✓ Use branches for features and experiments",
    "  ✓ Write descriptive branch names: feature-inflammation-analysis",
    "  ✓ Keep main branch stable and deployable",
    "  ✓ Use tags for releases and publications",
    "",
    "👥 COLLABORATION TIPS:",
    "  ✓ Use Pull Requests for code review",
    "  ✓ Link commits to issues for traceability",
    "  ✓ Document code and analysis steps",
    "  ✓ Use semantic versioning: v1.2.3",
    "",
    "🔒 DATA MANAGEMENT:",
    "  ✓ Never commit large data files",
    "  ✓ Use Git LFS for binary files if needed",
    "  ✓ Store data separately (institutional repositories)",
    "  ✓ Include data download/generation scripts",
    "",
    "🔧 CONFIGURATION FILES:",
    "  ✓ Commit requirements.txt or environment.yml",
    "  ✓ Include Makefile or setup scripts",
    "  ✓ Document software versions and dependencies",
]

for practice in best_practices:
    print(f"  {practice}")

# ============================================================
# Common Git Problems and Solutions
# ============================================================

print("\n=== Common Problems and Solutions ===")

troubleshooting = {
    "🚨 Accidentally committed sensitive data": [
        "git filter-branch --index-filter 'git rm --cached --ignore-unmatch secret.txt'",
        "# Or use BFG Repo-Cleaner for large repos",
        "# Then force push (be careful with shared repos)",
        "git push origin --force",
    ],
    "🔀 Merge conflicts": [
        "# Edit files to resolve conflicts",
        "# Look for <<<<<<< ======= >>>>>>> markers",
        "git add resolved-file.py",
        "git commit -m 'Resolve merge conflict in analysis'",
    ],
    "↩️ Undo last commit (not pushed)": [
        "git reset --soft HEAD~1  # Keep changes",
        "git reset --hard HEAD~1  # Discard changes",
    ],
    "🔄 Undo pushed commit": [
        "git revert HEAD  # Safe for shared repos",
        "git push origin main",
    ],
    "🌿 Delete branch that was merged": [
        "git branch -d feature-branch",
        "git push origin --delete feature-branch",
    ],
    "📊 Large files error": [
        "# Use Git LFS",
        "git lfs install",
        "git lfs track '*.csv'",
        "git add .gitattributes",
        "git add large-file.csv",
        "git commit -m 'Add large data file'",
    ],
    "🔄 Sync forked repository": [
        "git remote add upstream https://github.com/original/repo.git",
        "git fetch upstream",
        "git checkout main",
        "git merge upstream/main",
        "git push origin main",
    ],
}

print("🔧 Troubleshooting Guide:")
for problem, solutions in troubleshooting.items():
    print(f"\n{problem}:")
    for solution in solutions:
        print(f"  {solution}")

# ============================================================
# Sample .gitignore for Scientific Python Projects
# ============================================================

print("\n=== Sample .gitignore for Scientific Projects ===")

gitignore_content = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Scientific computing specific
*.h5
*.hdf5
*.mat
*.npz
*.pkl
*.pickle

# Data files (adjust as needed)
data/*.csv
data/*.xlsx
data/*.json
!data/sample_small.csv  # Include small sample files

# Results and output
results/
figures/
plots/
output/

# OS specific
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# IDE specific
.vscode/
.idea/
*.swp
*.swo
*~

# LaTeX
*.aux
*.bbl
*.blg
*.fdb_latexmk
*.fls
*.log
*.out
*.synctex.gz
*.toc
"""

print("📄 Recommended .gitignore content:")
print(gitignore_content)

# ============================================================
# Git Aliases for Efficiency
# ============================================================

print("\n=== Useful Git Aliases ===")

git_aliases = [
    "# Add these to your ~/.gitconfig file or run the commands",
    "",
    "git config --global alias.st status",
    "git config --global alias.co checkout",
    "git config --global alias.br branch",
    "git config --global alias.cm 'commit -m'",
    "git config --global alias.unstage 'reset HEAD --'",
    "git config --global alias.last 'log -1 HEAD'",
    "git config --global alias.visual '!gitk'",
    "git config --global alias.tree 'log --graph --oneline --all'",
    "git config --global alias.uncommit 'reset --soft HEAD~1'",
    "git config --global alias.recommit 'commit --amend --no-edit'",
    "",
    "# Usage examples:",
    "git st          # instead of git status",
    "git co main     # instead of git checkout main",
    "git cm 'Fix bug'  # instead of git commit -m 'Fix bug'",
    "git tree        # pretty log view",
]

print("⚡ Git Aliases for Efficiency:")
for alias in git_aliases:
    print(f"  {alias}")

# ============================================================
# Integration with Scientific Workflows
# ============================================================

print("\n=== Integration with Scientific Workflows ===")

scientific_integration = [
    "🔬 REPRODUCIBLE RESEARCH:",
    "  • Version control analysis scripts alongside data processing",
    "  • Tag releases that correspond to paper submissions",
    "  • Include computational environment specifications",
    "  • Document analysis pipelines in README files",
    "",
    "📊 DATA VERSIONING:",
    "  • Use Git LFS for large datasets when appropriate",
    "  • Store data download/generation scripts in repository",
    "  • Link to external data repositories (Zenodo, Figshare)",
    "  • Include data checksums for integrity verification",
    "",
    "📝 MANUSCRIPT COLLABORATION:",
    "  • Version control LaTeX/Markdown manuscripts",
    "  • Use branches for different manuscript versions",
    "  • Collaborate on figures and supplementary materials",
    "  • Track review comments and revisions",
    "",
    "🤝 TEAM COLLABORATION:",
    "  • Establish branching strategy for team projects",
    "  • Use Pull Requests for code review",
    "  • Document coding standards and contribution guidelines",
    "  • Set up continuous integration for testing",
    "",
    "📦 SOFTWARE RELEASES:",
    "  • Use semantic versioning for analysis software",
    "  • Create releases for published methods",
    "  • Include DOIs for citable software versions",
    "  • Maintain CHANGELOG.md for version history",
]

for item in scientific_integration:
    print(f"  {item}")

# ============================================================
# Quick Reference Commands
# ============================================================

print("\n=== Quick Reference Cheat Sheet ===")

quick_reference = {
    "Setup": ["git init", "git clone <url>", "git config --global user.name 'Name'"],
    "Daily Use": ["git status", "git add .", "git commit -m 'message'", "git push"],
    "Branching": [
        "git branch",
        "git checkout -b <branch>",
        "git merge <branch>",
        "git branch -d <branch>",
    ],
    "Remote": ["git pull", "git push", "git fetch", "git remote -v"],
    "History": ["git log", "git diff", "git show <commit>", "git blame <file>"],
    "Undo": [
        "git reset HEAD~1",
        "git revert <commit>",
        "git stash",
        "git checkout -- <file>",
    ],
}

print("📚 Quick Reference:")
for category, commands in quick_reference.items():
    print(f"\n{category}:")
    for cmd in commands:
        print(f"  {cmd}")

print("\n" + "=" * 60)
print("🎉 You're now equipped with Git and GitHub essentials!")
print("📖 Practice these commands with your inflammation analysis project")
print("🔗 Resources:")
print("  • Git documentation: https://git-scm.com/doc")
print("  • GitHub guides: https://guides.github.com")
print("  • Interactive Git tutorial: https://learngitbranching.js.org")
print("  • Git for Scientists: https://swcarpentry.github.io/git-novice")
print("💡 Remember: Version control is essential for reproducible research!")
