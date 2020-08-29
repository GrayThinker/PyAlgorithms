from setuptools import setup, find_packages

def long_desc():
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()
    return long_description

setup(
    name="pyalgo",
    version='0.0.1',
    description="Python algorithms and structures",
    long_description=long_desc(),
    url="https://github.com/GrayThinker/PyAlgorithms",
    author="Joseph Shatti",
    author_email="jshatti00@gmail.com",
    packages=find_packages(include=["PyAlgorithms", "PyAlgorithms.*"]),
    classifiers=[
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)