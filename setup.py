from setuptools import find_packages,setup 
from typing import List

hypen_e_dot = '-e .' 
def get_requirements(file_path:str)->List[str]:     # file path is a str and will return list and it is in the form of str
    '''
    this function will retur list of requirements
    ''' 
       
    requirements = []
    with open(file_path) as file_obj: # this will read the text of requirements file
        requirements = file_obj.readlines()  
        requirements = [req.replace("\n", "") for req in requirements] # while read the text of requriement.txt whenever the new line come it will print \n so we have to repalce the \n with space("") so by this code we can remove \n

        if hypen_e_dot in requirements:  # in requirement.txt we write "-e ." for enable setup.py and this "-e ." should not come while reading the text so we will remove "-e ."
            requirements.remove(hypen_e_dot) 

    return requirements   



# from setuptools import find_packages,setup
# from typing import List

# HYPEN_E_DOT='-e .'
# def get_requirements(file_path:str)->List[str]:
#     '''
#     this function will return the list of requirements
#     '''
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n","") for req in requirements]

#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
    
#     return requirements
    
   
setup(
name='mlproject',
version='0.0.1',
author='Deepak',
author_email='deepakgoyal3737@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')

)