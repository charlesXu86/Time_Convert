#-*- coding:utf-8 _*-
"""
@author:charlesXu
@file: setup.py
@desc: 设置
@time: 2019/05/23
"""
import pathlib
import os

from setuptools import setup, find_packages, convert_path

basedir = str(pathlib.Path(os.path.abspath(__file__)).parent)

def _version():
    ns = {}
    with open(convert_path("time_convert/version.py"), "r") as fh:
        exec(fh.read(), ns)
    return ns['__version__']

__version__ = _version()

with open("README.rst", "r") as lr:
    long_description = lr.read()

setup(
    name="time-convert",
    version=__version__,
    keywords=("time", "nlp"),
    description="Time convert for Chinese text",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="MIT Licence",
    url="https://github.com/charlesXu86/Time_Convert",
    author="xu",
    author_email="charlesxu86@163.com",
    packages={'time_convert': 'time_convert'},
    package_data={'time_convert': ['resource/*.json', 'resource/*.pkl', 'resource/*.txt']},
    include_package_data=True,
    platforms="any",
    install_requires=['regex>=2017',
                      'arrow==0.15.1'],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"]
)
print("Welcome to time convert!")