# Docker Cheat Sheet

This article highlights a list of useful Docker & Dockerfile commands.

[toc]

# Dockerfile Commands

```Dockerfile
# Pull base image for build
FROM ubuntu:latest

# Maintainer information
MAINTAINER Jian Yang

# Set temporary variables
ARG VAR=hotdog

# Set environment variables
ENV VAR hotdog

# Copy files from local directory to destination inside container
COPY src /usr/src/app

# Set working directory
WORKDIR /usr/src/app

# Allow inter-container communication on port
EXPORT 8000

# Run build command
RUN echo hotdog

# Run main command
CMD ["echo", "not hotdog"]
```

# Docker CLI Commands

## Build

### Build an image from Dockerfile in current working directory

```bash
docker build .
```

### Build an image from Dockerfile with name and tag

```bash
docker build -t <name>:<tag> .
docker build --tag <name>:<tag> .
```

### Show all locally stored images

```bash
docker image ls --all
```

### Remove an image from local storage

```bash
docker image rm <image name or ID>
```

## Run

### Run container using image

```bash
docker run <image name or ID>
```

### Run container in background

```bash
docker run -d <image name or ID>
docker run --detacted <image name or ID>
```

### Run container with environment variables

```bash
docker run -e VAR1="hotdog" -e VAR2="not hotdog" <image name or ID>
docker run --env VAR1="hotdog" --env VAR2="not hotdog" <image name or ID>
```

### Run container in interactive mode

```bash
docker run -it <image name or ID> /bin/bash
docker run --interactive --tty <image name or ID> /bin/bash
```

### Run container and publish container ports to the host

```bash
docker run -p <host port>:<container port> <image name or ID>
docker run --publish <host port>:<container port> <image name or ID>
```

### Run container and assign name

```bash
docker run --name <container name> <image name or ID>
```

### Show all containers

```bash
docker container ls --all
```

### Start container

```bash
docker start <container name or ID>
```

### Stop container

```bash
docker stop <container name or ID>
```

### Kill container

```bash
docker kill <container name or ID>
```

### Remove container

```bash
docker rm <container name or ID>
```
