#!/bin/bash

# Function to create folders
create_folders() {
  mkdir -p assets config data iac notebooks src tests
}

# Function to create Docker-related folders
create_docker_folders() {
  mkdir -p scripts dags logs plugins
  touch docker-compose.yaml
  touch Dockerfile
}

# Main script
echo "Creating folders: assets, config, data, iac, notebooks, src, tests"
create_folders

# Ask if Docker will be used
read -p "Will you be using Docker? (yes/no): " use_docker

if [ "$use_docker" == "yes" ]; then
  echo "Creating Docker-related folders: scripts, dags, logs, plugins"
  create_docker_folders
else
  echo "Skipping Docker-related folders."
fi

echo "Folders creation completed."