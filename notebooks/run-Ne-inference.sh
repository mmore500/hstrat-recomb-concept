#!/bin/bash

find . -name "Ne-inference-parameterization-*.yaml" -print0 | xargs -0 -I {} -P 7 bash -c 'echo "Processing: {}"; python3 -m papermill Ne-inference.ipynb "$(basename {} .yaml).ipynb" -f "{}"'
