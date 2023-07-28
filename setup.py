'''
The setup script is the centre of all activity in building, 
distributing, and installing modules using the Distutils. 
The main purpose of the setup script is to describe your module 
distribution to the Distutils, so that the various commands that 
operate on your modules do the right thing.
'''

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function wil return the list of requirements
    '''
    requirments = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name = 'mlprojects',
    version = '0.0.1',
    author = 'Shayan',
    author_email = 'shhaayan18@gmail.com',
    packages = find_packages(),
    install_requirements = get_requirements('requirements.txt')

)