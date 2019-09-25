#-*- coding:utf-8 _*-
"""
@author:charlesXu
@file: setup.py
@desc: 设置
@time: 2019/05/23
"""

from setuptools import setup

setup(
    name="time-convert",
    version="1.1.1",
    keywords=("time", "nlp"),
    description="Time convert for Chinese text",
    long_description="...",
    license="MIT Licence",
    url="https://github.com/charlesXu86/Time_Convert",
    author="xu",
    author_email="charlesxu86@163.com",
    packages={'time_convert': 'time_convert'},
    package_data={'time_convert': ['resource/*.json', 'resource/*.pkl', 'resource/*.txt']},
    include_package_data=True,
    platforms="any",
    install_requires=['regex>=2017',
                      'arrow>=0.10'],
    zip_safe=False,
    classifiers=[
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6'
        ]
)