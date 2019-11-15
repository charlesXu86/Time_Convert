# Time Convert

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
   
### To do list
   * 1、timedelta的拼接
   * 2、'一会儿'等口语化表述时间的提取
   * 3、过两天，明天吧
   * 4、下礼拜