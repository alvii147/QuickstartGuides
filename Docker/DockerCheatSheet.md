<h1>Docker Cheat Sheet</h1>

This article highlights a list of useful Docker & Dockerfile commands.

<h2>Contents</h2>

[toc]

## Dockerfile Commands

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
EXPOSE 8000

# Run build command
RUN echo hotdog

# Run main command
CMD ["echo", "not hotdog"]
```

## Docker CLI Commands

### Building Images

Build an image from Dockerfile in current working directory:

```bash
docker build .
```

Build an image from Dockerfile with name and tag:

```bash
docker build -t <name>:<tag> .
```

Show all locally stored images:

```bash
docker images -a
```

Remove an image from local storage:

```bash
docker image rm <image name or ID>
```

Remove all images from local storage:

```bash
docker image rm $(docker images -aq)
```

### Running Containers

Run container using image:

```bash
docker run <image name or ID>
```

Run container in background:

```bash
docker run -d <image name or ID>
```

Run container with environment variables:

```bash
docker run -e VAR1="hotdog" -e VAR2="not hotdog" <image name or ID>
```

Run container in interactive mode:

```bash
docker run -it <image name or ID> /bin/bash
```

Run container and publish container ports to the host:

```bash
docker run -p <host port>:<container port> <image name or ID>
```

Run container and assign name:

```bash
docker run --name <container name> <image name or ID>
```

Show all containers:

```bash
docker ps -a
```

Start container:

```bash
docker start <container name or ID>
```

Stop container:

```bash
docker stop <container name or ID>
```

Kill container:

```bash
docker kill <container name or ID>
```

Remove container:

```bash
docker rm <container name or ID>
```

Remove all containers:

```bash
docker rm $(docker ps -aq)
```
