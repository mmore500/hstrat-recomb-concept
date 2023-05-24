#!/bin/bash

find . -name "species-inference-parameterization-*.yaml" -print0 | xargs -0 -I {} -P 7 bash -c 'echo "Processing: {}"; python3 -m papermill species-inference.ipynb "$(basename {} .yaml).ipynb" -f "{}"'
