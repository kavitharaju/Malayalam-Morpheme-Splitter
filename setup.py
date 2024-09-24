from setuptools import setup, find_packages
from setuptools.command.install import install
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "Readme.md").read_text(encoding='utf-8')

setup(
    name='malayalam_morpheme_splitter',
    version='1.0.0-beta.2',
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
    author_email='Kavitha.Raju@bridgeconn.com, gladysann1307@gmail.com',
    description='An example based approach at separating suffixes in Malayalam text.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    project_urls={
        'Source Repository': 'https://github.com/kavitharaju/Malayalam-Morpheme-Splitter' 
    },
)