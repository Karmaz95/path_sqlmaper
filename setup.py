from setuptools import setup, find_packages

setup(
    name='path_sqlmaper',
    version='0.1',
    author='Karol Mazurek',
    author_email='karol.mazurek95@gmail.com',
    description='A simple Python script for URL wildcard generation',
    url='https://github.com/Karmaz95/path_sqlmaper',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'path_sqlmaper = path_sqlmaper:main'
        ]
    }
)