from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='malayalam_morpheme_splitter',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[],  
    entry_points={
        'console_scripts': [
            'malayalam_morpheme_splitter_install = malayalam_morpheme_splitter.install:main'
        ]
    },
    include_package_data=True,
    package_data={
        'malayalam_morpheme_splitter': ['data/morph_examples.py', 'data/malayalam_words.py'],
    },
    author='BCS Team',
    author_email='Kavitha.Raju@bridgeconn.com',
    description='An example based approach at seperating suffixes from Malayalam.',

    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
     project_urls={
           'Source Repository': 'https://github.com/kavitharaju/Malayalam-Morpheme-Splitter' 
    }
)
