from setuptools import setup, find_packages

print(find_packages())
setup(
    name = "smart_lib",
    version = "0.1",
    packages=find_packages(),
    install_requires=[]
)