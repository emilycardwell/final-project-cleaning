from setuptools import setup, find_packages

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='final-project-cleaning',
      description='cleaning functions',
      install_requires=requirements,
      packages=find_packages(),)
