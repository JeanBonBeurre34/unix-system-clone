
# Python Unix System Simulation



## Description

This project is a simple Python script that simulates basic Unix system functionalities. It's designed as an educational tool to help understand the workings of Unix-like systems at a fundamental level.

### Features

- Simulated file system with directories and files.
- Basic shell command interface.
- Supports commands like `ls`, `cd`, `mkdir`, `touch`, `echo`, `cat`, and `help`.
- Hidden mode to enable/disable the `help` command.

## Getting Started

### Prerequisites

- Python 3.8 or later.

### Installation

Clone the repository or download the source code to your local machine.

```bash
git clone https://github.com/JeanBonBeurre34/unix-system-clone.git
cd unix-system-clone
```

### Running the Simulation

Execute the script from the command line:

```bash
python unix-system.py
```

## Usage

Once you run the script, you will enter an interactive shell-like environment where you can execute the supported commands. For example:
- **ls** - Lists the contents of the current directory.
- **cd directory_name** - Changes the current directory.
- **mkdir directory_name** - Creates a new directory.
- **touch file_name** - Creates a new file.
- **echo "text" > file_name** - Adds text to a file.
- **cat file_name** - Displays the content of a file.
- **help** - Displays available commands (if not in hidden mode).
- **exit** - Exits the simulation.

## Docker Support

This project includes a Dockerfile for easy setup and deployment in a Docker container. Follow these steps to build and run the simulation using Docker:

### Build the Docker Image in local from repository

Navigate to the directory containing the Dockerfile and run the following command to build the Docker image:

```bash
docker build -t unix-simulation .
```
This command builds a Docker image named unix-simulation using the Dockerfile in the current directory.

### Build the Docker Image from docker hub
Just run the command to pull the docker image from docker hub
```bash
docker pull reg0l1/unix-simulati0n
```
This command builds a Docker image from docker hub.

### Run the container
After the image has been built, run it with the following command:
```bash
docker run -it unix-simulation
```
This command starts a Docker container based on the **unix-simulation** image. The **-it** flags attach an interactive terminal to the container, allowing you to interact with the Unix simulation shell.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.
