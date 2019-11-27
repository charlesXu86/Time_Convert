Time Convert
====================


|Build Status| |Coverage Status| |Version Status| |Python Versions| |Downloads|


### Introduction
中文语义时间提取转换

### Install
`pip install time-convert`

### Usage

eg1:

`from time_convert import TimeNormalizer`

`tc = TimeNormalizer()`

`msg = `明天去你家'

`res = tc.parse(msg)`

`print``(res)`

`{'key': '明天', 'type': 'timestamp', 'date': '2019-09-26 00:00:00'}`



eg2：

`from time_convert import TimeNormalizer`

`tc = TimeNormalizer()`

`msg = `明天去你家'

`timeBase=`2013-02-28 16:30:29`

`res = tc.parse(msg, timeBase)`

`print``(res)`

`{'key': '明天', 'type': 'timestamp', 'date': '2013-03-01 00:00:00'}`


### 返回值类型说明
Time_Convert总的会返回四种类型的情况：
   * 1、timespan
   * 2、timestamp
   * 3、timedelta
   * 4、error

### Mark
   * 1、时间解析的默认basetime时间为请求的当前时间。
   * 2、也可以指定basetime，basetime的格式为：**YYYY-MM-DD 00:00:00**

NEWS
----

### To do list
   * 1、timedelta的拼接
   * 2、'一会儿'等口语化表述时间的提取
   * 3、过两天，明天吧
   * 4、下礼拜

.. |Build Status| image:: https://github.com/charlesXu86/Time_Convert?branch=master
   :target: https://github.com/charlesXu86/Time_Convert
.. |Coverage Status| image:: https://coveralls.io/repos/kpe/bert-for-tf2/badge.svg?branch=master
   :target: https://coveralls.io/r/kpe/bert-for-tf2?branch=master
.. |Version Status| image:: https://badge.fury.io/py/bert-for-tf2.svg
   :target: https://badge.fury.io/py/bert-for-tf2
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/bert-for-tf2.svg
.. |Downloads| image:: https://img.shields.io/pypi/dm/bert-for-tf2.svg
.. |Twitter| image:: https://img.shields.io/twitter/follow/siddhadev?logo=twitter&label=&style=
   :target: https://twitter.com/intent/user?screen_name=siddhadev