#!/bin/bash

# Set the image name
IMAGE_NAME="playwright-test"
VENV_DIR=".venv"

# Function to build the Docker image
build_image() {
    echo "Building Docker image..."
    docker build -t $IMAGE_NAME .
}

# Function to run tests in the Docker container
run_tests_in_docker() {
    echo "Running tests in Docker with command: pytest $*"
    docker run --rm -it -v "$(pwd)":/app -w /app $IMAGE_NAME pytest "$@"
}

# Function to create a virtual environment and install dependencies
setup_local_env() {
    echo "Setting up virtual environment..."
    if [ ! -d "$VENV_DIR" ]; then
        python3 -m venv $VENV_DIR
        echo "Virtual environment created at $VENV_DIR."
    else
        echo "Virtual environment already exists."
    fi

    echo "Activating virtual environment..."
    source $VENV_DIR/bin/activate

    echo "Installing dependencies..."
    pip install -r requirements.txt
}

# Function to run tests locally
run_tests_local() {
    echo "Running tests locally with command: pytest $*"
    source $VENV_DIR/bin/activate
    pytest "$@"
}

# Function to clean the virtual environment
clean_env() {
    echo "Removing virtual environment..."
    rm -rf $VENV_DIR
    echo "Virtual environment removed."
}

# Main script execution
if [ "$1" == "build" ]; then
    build_image
elif [ "$1" == "test-docker" ]; then
    shift
    run_tests_in_docker "$@"
elif [ "$1" == "setup-local-env" ]; then
    shift
    setup_local_env
elif [ "$1" == "test-local" ]; then
    shift
    run_tests_local "$@"
elif [ "$1" == "clean" ]; then
    clean_env
else
    echo "Usage: $0 {build-image|test-docker|setup-local-env|test-local [pytest_options]|clean}"
    exit 1
fi