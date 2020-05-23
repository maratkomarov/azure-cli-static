#!/bin/bash


docker run --rm \
    -v $(pwd):/shared \
    -e AZURE_CORE_COLLECT_TELEMETRY=0 \
    --entrypoint /bin/sh six8/pyinstaller-alpine -c "
        apk add --update gcc make python3 python3-dev musl-dev libffi-dev openssl-dev;
        pip3 install azure-cli;
        az extension add --system --name resource-graph;
        pyinstaller /shared/az.spec;
        cp dist/az /shared/
    "

