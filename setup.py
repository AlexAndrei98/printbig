from setuptools import setup

setup(
    # Needed to silence warnings
    name='alexUtil',
    url='https://github.com/AlexAndrei98/testpackage',
    author='Alex Andrei',
    author_email='alexandrei1998@hotmail.it',    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    license='MIT',
    description='An example of my python package',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.txt').read(),
)
