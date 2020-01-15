Time_Convert
====================


|Build Status| |Coverage Status| |Version Status| |Python Versions| |Downloads|


Introduction
>>>>>>>>>>>>>>>>>>>>

Time_Convert是一个中文语义时间提取转换工具，他参考的项目是微软的时间提取代码。（由于时间比较久，找不到链接了）。目前该工具基本可以
提取出对话文本中提及的时间相关的短语，例如：今天、明天、下周、下个月等等，并归一化成相对应的时间日期。可以为很多NLP的基础分析任务提供极大的便利。


Install
>>>>>>>>>>>

::

   pip install time-convert

   import time_convert as tv
   print(tv.__version__)    # 查看版本信息


Usage
---------------------

eg1:

.. code:: python

      from time_convert import TimeNormalizer

      tc = TimeNormalizer()

      msg = '明天去你家'

      res = tc.parse(msg)

      print(res)

      {'key': '明天', 'type': 'timestamp', 'date': '2019-09-26 00:00:00'}



eg2：

.. code:: python

      from time_convert import TimeNormalizer

      tc = TimeNormalizer()

      msg = `明天去你家'

      timeBase = '2013-02-28 16:30:29'

      res = tc.parse(msg, timeBase)

      print(res)

      {'key': '明天', 'type': 'timestamp', 'date': '2013-03-01 00:00:00'}

Mark
>>>>>>>>>>

   * 1、时间解析的默认basetime时间为请求的当前时间。

   * 2、也可以指定basetime，basetime的格式为：**YYYY-MM-DD 00:00:00**

   * 3、如果不指定basetime，则默认basetime为当前请求时间


返回值类型说明
===================

Time_Convert总的会返回四种类型的情况：

   * 1、timespan
   * 2、timestamp
   * 3、timedelta
   * 4、error


Update NEWS
===================

    * 2019.10  v1版本打包上线

    * 2020.1   更新python版本兼容问题


To do list
===================

   * 1、timedelta的拼接
   * 2、'一会儿'等口语化表述时间的提取
   * 3、过两天，明天吧
   * 4、下礼拜
   * 5、在返回关键词的时候添加上index

.. |Build Status| image:: https://travis-ci.org/charlesXu86/Time_Convert.svg?branch=master
   :target: https://travis-ci.org/charlesXu86/Time_Convert
.. |Coverage Status| image:: https://coveralls.io/repos/github/charlesXu86/Time_Convert/badge.svg
    :target: https://coveralls.io/github/charlesXu86/Time_Convert
.. |Version Status| image:: https://badge.fury.io/py/time-convert.svg
   :target: https://badge.fury.io/py/time-convert
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/time-convert.svg
.. |Downloads| image:: https://img.shields.io/pypi/dm/time-convert.svg