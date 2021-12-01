"""
general utilities for advent of code
"""

import os.path


def read_to_string(in_file_path):
    """reads a file to a string"""
    assert os.path.isfile(in_file_path)
    with open(in_file_path, 'r', encoding='utf-8') as in_file:
        data_str = in_file.read()
    assert len(data_str) > 0
    return data_str
