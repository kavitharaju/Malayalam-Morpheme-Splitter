import os
import shutil
import pkg_resources

def main():
   
    target_dir = os.getcwd()

   
    data_file_1 = pkg_resources.resource_filename('malayalam_morpheme_splitter', 'data/morph_examples.py')
    data_file_2 = pkg_resources.resource_filename('malayalam_morpheme_splitter', 'data/malayalam_words.py')

  
    destinationfile_1 = os.path.join(target_dir, 'morph_examples.py')
    destinationfile_2 = os.path.join(target_dir, 'malayalam_words.py')

   
    shutil.copy2(data_file_1, destinationfile_1)
    shutil.copy2(data_file_2, destinationfile_2)

    print(f'morph_examples.py has been installed to {destinationfile_1}')
    print(f'malayalam_words.py has been installed to {destinationfile_2}')