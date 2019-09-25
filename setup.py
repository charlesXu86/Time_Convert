#-*- coding:utf-8 _*-
"""
@author:charlesXu
@file: setup.py
@desc: 设置
@time: 2019/05/23
"""

from setuptools import setup

setup(
    name="Time_Convert",
    version="1.1.0",
    keywords=("time", "nlp"),
    description="Time convert for Chinese test",
    long_description="...",
    license="MIT Licence",
    url="http://test.com",
    author="xu",
    author_email="charlesxu86@163.com",
    packages=['', 'resource'],
    package_data={'resource': ['*.json', '*.pkl']},
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