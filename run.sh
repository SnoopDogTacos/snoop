#!/bin/bash
docker build -t snoop .
docker run -d --restart=unless-stopped --env-file docker.env --name snoop snoop

