import os
import shutil
from setuptools import setup, find_packages
from setuptools.command.install import install
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "Readme.md").read_text(encoding='utf-8')

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        mms_dir = os.path.expanduser('~/.mms_data')
        os.makedirs(mms_dir, exist_ok=True)

        pycache_dir = os.path.join(mms_dir, '__pycache__')
        if os.path.exists(pycache_dir):
            shutil.rmtree(pycache_dir)
            print(f"Removed existing __pycache__ from {mms_dir}")

        data_dir = os.path.join(os.path.dirname(__file__), 'malayalam_morpheme_splitter', 'data')

        shutil.copy(os.path.join(data_dir, 'morph_examples.py'), mms_dir)
        shutil.copy(os.path.join(data_dir, 'malayalam_words.py'), mms_dir)

        super().run()

setup(
    name='malayalam_morpheme_splitter',
    version='1.0.0-beta.1',
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
    cmdclass={
        'install': PostInstallCommand,
    },
)