"""
install.py

This module provides an installation script 
for setting up the necessary data files for 
the Malayalam Morpheme Splitter. 
"""
import os
import shutil
import pkg_resources

def main():
    """
    Copies the 'morph_examples.py' and 'malayalam_words.py' files 
    from the package data directory to a hidden directory in the user's home directory.
    """
    mms_dir = os.path.expanduser("~/.mms_data")
    os.makedirs(mms_dir, exist_ok=True)
    path_1 = os.path.join(mms_dir, "morph_examples.py")
    path_2 = os.path.join(mms_dir, "malayalam_words.py")
    data_file_1 = pkg_resources.resource_filename('malayalam_morpheme_splitter', 'data/morph_examples.py')
    data_file_2 = pkg_resources.resource_filename('malayalam_morpheme_splitter', 'data/malayalam_words.py')
    shutil.copy2(data_file_1, path_1)
    shutil.copy2(data_file_2, path_2)
    print(f'morph_examples.py has been installed to {path_1}')
    print(f'malayalam_words.py has been installed to {path_2}')

