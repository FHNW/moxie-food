from setuptools import setup, find_packages


install_requires = open('requirements.txt').readlines()

setup(name='moxie-food',
    version='0.1',
    packages=find_packages(),
    description='Food module for Moxie',
    author='FHNW',
    author_email='webmaster@fhnw.ch',
    url='https://github.com/FHNW/moxie-food',
    include_package_data=True,
    setup_requires=["setuptools"],
    install_requires=install_requires,
    test_suite="moxie_food.tests",
)
