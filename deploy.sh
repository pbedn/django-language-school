#!/usr/bin/env bash

ssh -o StrictHostKeyChecking=no -tv $SSH_USER@$SSH_HOST << EOF

echo "0. Setting virtual env path and repo directory"
cd $SERVER_REPO_PATH
source $SERVER_VENV_ACTIVATE_PATH
echo "1. Fetching all remotes"
git fetch --all
echo "2. Checking out using force.."
git checkout --force origin/master
echo "3. Updating requirements"
poetry install
echo "4. Migrating database"
./manage.py migrate
echo "Done!"

EOF
