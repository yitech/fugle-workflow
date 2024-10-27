#!/bin/bash

# Define output folder
OUTPUT_DIR="fugledata-go"

# Step 1: Create or empty the "fugle-go-client" directory
if [ -d "$OUTPUT_DIR" ]; then
    rm -rf "${OUTPUT_DIR:?}/"*
else
    mkdir "$OUTPUT_DIR"
fi

# Step 2: Generate initial client library from the local OpenAPI server
openapi-generator-cli generate -i https://postgrest.lynxlinkage.com \
    -g go \
    -o "./$OUTPUT_DIR" \
    --package-name fugledata \
    --git-host github.com \
    --git-user-id yitech \
    --git-repo-id fugledata-go

cd "$OUTPUT_DIR" && chmod +x ./git_push.sh && /bin/sh ./git_push.sh yitech fugledata-go "minor update" "github.com"

echo "Client code has been successfully generated and modified in ./$OUTPUT_DIR"