from setuptools import find_packages,setup
#from typing import List


def get_requirements()->list[str]:
    
    requirement_list :list[str] = []

    return requirement_list

setup(
    name='sensor',
    version="1.0.1",
    author="Sandeep Deshmukh",
    author_email="sandeepsdeshmukh1@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements(),
)