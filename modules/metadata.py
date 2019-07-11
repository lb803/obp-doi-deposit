#!/usr/bin/env python3
import os
import json

class Metadata:
    def __init__(self, metadata_file):
        # Get metadata file absolute path
        metadata_path = os.path.abspath(metadata_file)

        # Check that the file is in place
        if not os.path.exists(metadata_path):
            raise ValueError("The file {} doesn't exist".format(metadata_path))

        with open(metadata_path, 'r') as f:
            self.metadata = json.load(f)
            print(self.metadata)
