#!/bin/bash

# Initialize tasks for setting up the workspace
# Author: Matt Rudge

echo "Initializing tasks..."

# Check if GITPOD_GIT_USER_NAME and GITPOD_REPO_ROOT are set
if [[ -z "$GITPOD_GIT_USER_NAME" ]] || [[ -z "$GITPOD_REPO_ROOT" ]]; then
    echo "Error: GITPOD_GIT_USER_NAME or GITPOD_REPO_ROOT is not set."
    exit 1
fi

# Ensure README.md exists before trying to modify it
if [[ ! -f "${GITPOD_REPO_ROOT}/README.md" ]]; then
    echo "Error: README.md not found in the repository root."
    exit 1
fi

# Replacing the placeholder USER_NAME with the Gitpod Git user name in README.md
echo "Updating README.md with Gitpod Git user name..."
if ! sed -i "s/USER_NAME/$GITPOD_GIT_USER_NAME/g" "${GITPOD_REPO_ROOT}/README.md"; then
    echo "Error: Failed to update README.md."
    exit 1
fi

# Create .sqliterc configuration file for SQLite
echo "Creating .sqliterc file for SQLite..."
echo ".headers on" > ~/.sqliterc
echo ".mode column" >> ~/.sqliterc

# Check if the .sqliterc file was created successfully
if [[ -f ~/.sqliterc ]]; then
    echo ".sqliterc file created successfully."
else
    echo "Error: Failed to create .sqliterc file."
    exit 1
fi

echo "Your workspace is ready to use. Happy coding!"
