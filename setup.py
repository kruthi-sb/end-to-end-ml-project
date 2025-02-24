from setuptools import find_packages, setup
from typing import List # it is used to specify the type of the variable

HYPHEN_E_DOT = '-e .' # it is the string that is used to check if the line in the requirements.txt file is a local package or not.
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #reads the content insode the requirements.txt file and stores it in the list. (this will include /n at the end of each line)
        requirements=[req.replace("\n","") for req in requirements] # it removes the /n from the end of each line.
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

# meta data of the project
setup(
    name='mlproject',
    version='0.0.1',
    author='Kruthi S B',
    author_email='kruthi.banakar@gmail.com',
    packages=find_packages(), # it goes through the directory and finds all '__init__.py' files and the folders they're in and builds the folder and includes them in the package. we can separately import the built folder.
    install_requires=get_requirements('requirements.txt') # it reads the requirements.txt file and installs the packages mentioned in the file.

)