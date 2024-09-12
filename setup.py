import os
import re
import sys
from setuptools import setup, find_packages

# Step 1: Get the version from src/rpg_world/__version__.py
def get_version():
    version_file = os.path.join('src', 'rpg_world', '__version__.py')
    with open(version_file) as f:
        version_content = f.read()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_content, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")

# Step 2: Get install_requires from requirements.txt
def get_requirements():
    requirements_file = 'requirements.txt'
    with open(requirements_file) as f:
        return f.read().splitlines()

# Step 3: Get python_requires from the current Python version
def get_python_version():
    return f">={sys.version_info.major}.{sys.version_info.minor}"

# Setup function
setup(
    name='rpg_world',  # Replace with your package's name
    version=get_version(),  # Dynamically get version from __version__.py
    description='A flexible RPG combat system for customizable battles and balancing',  # Brief description
    author='Andrew Ruba',  # Replace with your name
    author_email='ruba.andrew@gmail.com',  # Replace with your email
    url='https://github.com/andrewruba/rpg_world',  # Replace with your project's URL
    package_dir={'': 'src'},  # Point to the 'src' folder
    packages=find_packages(where='src'),  # Automatically find all packages in the 'src' directory
    install_requires=get_requirements(),  # Dynamically get install_requires from requirements.txt
    python_requires=get_python_version(),  # Dynamically get python_requires from the active environment
    classifiers=[            # Optional metadata for better project categorization
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
)
