#!/usr/bin/env python

from setuptools import setup

setup(name='target-csv',
      version='0.3.0',
      description='Singer.io target for writing CSV files',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['target_csv'],
      install_requires=[
          "singer-python>=5.0.12",
      ],
      entry_points='''
          [console_scripts]
          target-csv=target_csv:main
      ''',
)
