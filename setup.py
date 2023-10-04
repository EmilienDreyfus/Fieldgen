from setuptools import setup, find_packages

setup(
    name='fieldgen',
    version='0.1',
    author='Emilien Dreyfus',
    description='Un package pour l\'automatisation dans les factories.',
    packages=find_packages(),
    install_requires=[
        "factoryboy"
    ],
)
