#-*- coding:utf-8 _*-
"""
@author:charlesXu
@file: setup.py
@desc: 设置
@time: 2019/05/23
"""
import pathlib
import os

from setuptools import setup

basedir = str(pathlib.Path(os.path.abspath(__file__)).parent)

DESC_FILT = basedir + '/README.md'
setup(
    name="time-convert",
    version="1.2.2",
    keywords=("time", "nlp"),
    description="Time convert for Chinese text",
    long_description=DESC_FILT,
    license="MIT Licence",
    url="https://github.com/charlesXu86/Time_Convert",
    author="xu",
    author_email="charlesxu86@163.com",
    packages={'time_convert': 'time_convert'},
    package_data={'time_convert': ['resource/*.json', 'resource/*.pkl', 'resource/*.txt']},
    include_package_data=True,
    platforms="any",
    install_requires=['regex>=2017',
                      'arrow==0.13.1'],
    zip_safe=False,
    classifiers=[
            'Programming Language :: Python :: 3.x'
        ]
)
print("Welcome to time convert!")