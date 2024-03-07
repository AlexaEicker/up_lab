from setuptools import setup, find_packages

classifiers =[
	'Development Status :: 5 - Production/Stable',
	'Intended Audience :: Higher Education',
	'Operating system :: Microsoft :: Windows :: Windows 10',
	'Licence :: MIT Licence',
	'Programming Language :: Python :: 3']

setup(
	name='up_lab',
	version = '0.0.1',
	description='Collection of useful commands and analysing functions for the physics laboratory at University of Potsdam, Germany',
	long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
	url='',
	author='Alexa Eicker',
	classifiers=classifiers,
	keywords=['laboratory','analyse','plot','python', 'Germany','Potsdam','university'],
	packages=find_packages(),
	install_requires=['matplotlib', 'numpy', 'scipy', 'pandas', 'sympy']
)