from setuptools import setup

setup(
    name='tableaudocumentapi',
    version='0.8.4',
    author='Tableau',
    author_email='thierry@turpin.be',
    url='https://github.com/thierryturpin/document-api-python',
    packages=['tableaudocumentapi'],
    license='MIT',
    description='A Python module for working with Tableau files.',
    test_suite='test',
    install_requires=['lxml', 'packaging']
)
