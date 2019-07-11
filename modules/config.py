#!/usr/bin/env python3
import os
import configparser

class Config:
        def __init__(self):
                # Get config file absolute path
                config_file_path = os.path.abspath('config.ini')

                # Check that the file is in place
                if not os.path.exists(config_file_path):
                        raise ValueError("The file {} doesn't exist" \
                                         .format(config_file_path))
                
                self.config = configparser.ConfigParser()
                self.config.read(config_file_path)

        def get_config(self, section, item):
                return self.config.get(section, item)
