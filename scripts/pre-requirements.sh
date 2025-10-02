#!/bin/bash

function check_uv_installed() {
    if ! command -v uv &> /dev/null; then
        echo "uv is not installed. Please go to https://docs.astral.sh/uv/getting-started/installation/."
        return 1
    fi
    return 0
}

check_uv_installed
