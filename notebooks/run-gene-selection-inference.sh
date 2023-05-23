#!/bin/bash

find . -name "gene-selection-inference-parameterization-*.yaml" -print0 | xargs -0 -I {} -P 5 bash -c 'echo "Processing: {}"; python3 -m papermill gene-selection-inference.ipynb "$(basename {} .yaml).ipynb" -f "{}"'
