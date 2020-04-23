# -*- coding: utf-8 -*-

import os
from setuptools import Command, setup

packages = ['function_profiling']
for root, dirs, _ in os.walk('function_profiling', followlinks=True):
    if 'tests' in root:
        continue
    packages += [os.path.join(root, dir_name) for dir_name in dirs if 'tests' not in dir_name]


class PyTest(Command):
    user_options = [
        ('pytest-args=', 'a', 'Arguments to pass to py.test')
    ]
    
    def initialize_options(self):
        self.pytest.args = []

    def finalize_options(self):
        pass

    def run(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        raise SystemExit(errno)


setup(
    name='function-profiling',
    version='0.1.0',
    description='Function profiling library for python',
    long_description='Function profiling library for python based on cProfile',
    author='',
    author_email='',
    platforms=['linux_x86_64'],
    packages=packages,
    install_requires=[
        'pandas'
    ],
    extras_require={
        'dev': [
            'flake8',
            'pytest'
        ]
    },
    tests_require=[
        'pytest'
    ],
    cmdclass={'test': PyTest},
    
)
