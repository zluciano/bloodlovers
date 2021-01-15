#!/bin/bash

docker build -t joseluciano .
docker stop joseluciano
docker run -d --rm -p 8002:8000 \
        --env-file $HOME/joseluciano.env \
        --name joseluciano \
        -v $(pwd)/dkdata:/dkdata \
        joseluciano start.sh
