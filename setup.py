from setuptools import setup, find_packages

classifiers =[
	'Development Status :: 2 - Pre-Alpha',
	'Intended Audience :: Education',
	'Operating system :: Microsoft :: Windows :: Windows 10',
	'Licence :: MIT Licence',
	'Programming Language :: Python :: 3',
    'Topic :: Scientific/Engineering :: Physics']

setup(
	name='up_lab',
	version = '0.0.1',
	description='Collection of useful commands and analysing functions for the physics laboratory at University of Potsdam, Germany',
	long_description=open('README.md','r',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
	url='https://github.com/AlexaEicker/up_lab',
	author='Alexa Eicker',
	classifiers=classifiers,
	keywords=['laboratory','analyse','plot','python', 'Germany','Potsdam','experiment','experimental physics'],
	packages=find_packages(),
	install_requires=['matplotlib', 'numpy', 'scipy', 'pandas', 'sympy']
)

#TODO: check wheter long_description works