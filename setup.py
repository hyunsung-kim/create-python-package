import io
from setuptools import setup, find_packages
 

# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(name='custom-mathlib',
    version='0.0.3',
    url='https://github.com/hyunsung-kim/create-python-package.git',
    license='MIT',
    author='Hyunsung Kim',
    author_email='hyunsung.kim@superb-ai.com',
    description='Math Library for custom mathmatics',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['tests']),
    long_description=long_description(),
    install_requires=['numpy'],
    zip_safe=False
)
