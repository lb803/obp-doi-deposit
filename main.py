#!/usr/bin/env python3
import json
import os

# DEBUG open the example file
input_metadata = os.path.join(os.path.dirname(__file__),
                              'example-monograph.json')

with open(input_metadata, 'r') as f:
    metadata = json.load(f)
    print(metadata)
