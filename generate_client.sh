#!/bin/bash

# Define output folders
OUTPUT_DIR_GO="fugledata-go"
OUTPUT_DIR_PY="fugledata-py"

# Function to generate client code
generate_client() {
    local output_dir=$1
    local language=$2
    local package_name=$3
    local repo_id=$4

    # Step 1: Create or empty the output directory
    if [ -d "$output_dir" ]; then
        rm -rf "${output_dir:?}/"*
    else
        mkdir "$output_dir"
    fi

    # Step 2: Generate initial client library from the local OpenAPI server
    openapi-generator-cli generate -i http://localhost:3000 \
        -g "$language" \
        -o "./$output_dir" \
        --package-name "$package_name" \
        --git-host github.com \
        --git-user-id yitech \
        --git-repo-id "$repo_id"

    cd "$output_dir" && chmod +x ./git_push.sh && /bin/sh ./git_push.sh yitech "$repo_id" "minor update" "github.com"
    cd ..
    
    echo "Client code has been successfully generated and pushed for $language in ./$output_dir"
}

# Generate Go client
generate_client "$OUTPUT_DIR_GO" "go" "fugledata" "fugledata-go"

# Generate Python client
generate_client "$OUTPUT_DIR_PY" "python" "fugledata" "fugledata-py"