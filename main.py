#!/usr/bin/env python3
import argparse
import sys

sys.path.append('modules')
from config import Config
from metadata import Metadata

# Parse command line arguments
parser = argparse.ArgumentParser(description='obp-doi-deposit')
parser.add_argument('metadata',
                    help = 'JSON file where input metadata is stored')
args = parser.parse_args()

# Create objects to work with
conf = Config()
meta = Metadata(args.metadata)
