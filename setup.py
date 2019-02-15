from setuptools import setup

setup(
    # Needed to silence warnings
    name='alexUtil',
    url='',
    author='Alex Andrei',
    author_email='alexandrei1998@hotmail.it',    # Needed for dependencies
    install_requires=['numpy','re','pickle','string'],
    # *strongly* suggested for sharing
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('READEME.txt').read(),
)
