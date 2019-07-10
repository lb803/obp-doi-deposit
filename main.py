#!/usr/bin/env python3
import json
import os
import argparse

parser = argparse.ArgumentParser(description='obp-doi-deposit')
parser.add_argument('metadata',
                    help = 'JSON file where input metadata is stored')

args = parser.parse_args()

# Store input file path and verify that it extsts
input_metadata = os.path.abspath(args.metadata)
if not os.path.exists(input_metadata):
    raise ValueError("The file {} doesn't exist".format(input_metadata))

with open(input_metadata, 'r') as f:
    metadata = json.load(f)
    print(metadata)
