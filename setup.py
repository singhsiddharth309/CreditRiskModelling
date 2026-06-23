from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
        This function will return list of requirements
    """
    try:
        requirements_list:List[str] = []
        with open("requirements.txt",'r') as file:
            #read lines from file
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                #ignore empty line and -e .
                if requirement and requirement!='-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("Unable to find the requirements.txt file.")
    return requirements_list

setup(
    name = "CreditRiskModelling",
    version = "0.0.1",
    author = "Siddharth Singh",
    author_email = "singh.siddharth.0307@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)
