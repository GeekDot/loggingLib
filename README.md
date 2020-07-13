<h2 align= center> loggingLib 日志处理库 </h2>

<h5 align=right> 张懿 </h5>
<p align=right> 2019-09-16 </p>

### 一、概述

`loggingLib` 是日志处理库，依赖 `os`、`datetime`、`logging` 库，`loggingLib` 是对 `logging` 库进行二次封装，使用更加方便简洁，只用一行就可以X写入日志

下面是对 `loggingLib` 的详解，如想快速使用，请移步 `demo.py` 模块，里面有 `loggingLib` 的使用 `demo`

### 二、安装

`loggingLib` 是以源码的方式呈现，使用的时候直接导入即可

	from loggingLib import log
      
### 三、使用

#### 1. `loggingLib` 基础

`loggingLib` 提供了获取 `loggr` 的方法：`get`

	logger = log.get(__file__)

方法原型：

	get(name, level='info', layer=3)
	
- `name`：文件名称，必要参数，参数是每个文件的 `__file__`

- `level`：设置日志级别，默认为 `info`，`6` 类日志级别分别是：`debug`、`info`、`warning`、`error`、`critical`

- `layer`：目录层级，是控制日志文件名的参数，默认为 `3` 层

譬如程序的路径如下：

	/Users/setup/Documents/GeeKCode/calendar/demo.py

`layer=3` 的文件名称是：

	GeeKCode_calendar_demo_0000_00_00_00.log
	
`0000_00_00_00` 代表的含义是日期和小时：`2019-09-16_11`

`layer=2` 的文件名称是：

	calendar_demo_0000_00_00_00.log
	
如果 `layer` 参数有误，或者是 `layer` 的值超出了它本身的目录层级，那么文件名称就按照绝对路径下各个目录的名称命名

	Users_setup_Documents_GeeKCode_calendar_demo_0000_00_00_00.log
	
#### 2. 程序中使用 `loggingLib`

上述介绍的是 `loggingLib` 是日志处理库的一些使用介绍、方法、参数和相关命名，接下来是在程序中如何使用 `loggingLib`

	#!/usr/bin/env python3
	# -*- coding: UTF-8 -*-
	
	from loggingLib import log
	
	logger = log.get(__file__)
	
	
	def main_1():
	    logger.debug('debug')
	    logger.info('info')
	    logger.warning('warning')
	
	
	def main_2():
	    logger.error('error')
	    logger.critical('critical')
	
	
	main_1()
	main_2()

#### 3. 自定义日志路径

上述使用 `loggingLib` 日志文件都是在当前目录下存储的，但是在实际开发过程中日志都是在同一的日志路径下，如：`/var/log`，那 `loggingLib` 如何修改日志路径呢？

有两种方式，局部和全局的方式

局部修改：

只影响这一个文件的日志输出，在导入库的时候不导入 `log` 属性，而是导入类

	#!/usr/bin/env python3
	# -*- coding: UTF-8 -*-

	from loggingLib import LoggingLib
	
	
	log = LoggingLib('/home/setup/Downloads')
	logging = log.get(__file__)
	
	
	def main_3():
	    logging.debug('debug')
	    logging.info('info')
	    logging.warning('warning')
	
	
	def main_4():
	    logging.error('error')
	    logging.critical('critical')
	
	
	main_3()
	main_4()

然后在实例化类的时候需要传入要保存日志的绝对路径

	log = LoggingLib('/home/setup/Downloads')
	
接下来使用的方式和之前就一样了

全局修改：

全局修改需要在 `loggingLib.py` 文件中，实例化类的时候需要传入要保存日志的绝对路径
	
	    # 获取 logger
	    def get(self, name, level='info', layer=3):
	
	        # 获取日志文件名
	        log_file = self._dir_layer(name, layer)
	
	        # 设置日志级别，默认 INFO
	        log_level = self.level_list[level]
	        self.logger.setLevel(log_level)
	
	        # 文件输出流
	        self._file_stream(log_file)
	
	        # 屏幕输出流
	        self._screen_stream()
	
	        return self.logger
	
	
	log = LoggingLib()
	
将最后一行的

	log = LoggingLib()
		
修改为

	log = LoggingLib('/home/setup/Downloads')
		
即可

根据全局和局部日志路径的设定，可以灵活的绝对日志存储路径

### 四、日志文件内容详解

先看下刚才我们执行 `demo.py` 程序输出的日志，日志格式如下：

	2019-09-16 11:50:45 - [INFO]: demo.main_1(line:11) ==> '/Users/zhangyi/DemoCode/PythonToolLib/日志处理/demo.py' - info
	2019-09-16 11:50:45 - [WARNING]: demo.main_1(line:12) ==> '/Users/zhangyi/DemoCode/PythonToolLib/日志处理/demo.py' - warning
	2019-09-16 11:50:45 - [ERROR]: demo.main_2(line:16) ==> '/Users/zhangyi/DemoCode/PythonToolLib/日志处理/demo.py' - error
	2019-09-16 11:50:45 - [CRITICAL]: demo.main_2(line:17) ==> '/Users/zhangyi/DemoCode/PythonToolLib/日志处理/demo.py' - critical
	
日志内容以 `-` 为分隔符，分为三个部分

第一部分，是日志输出的时间和日期，精确到秒

第二部分，在两个 `-` 中间的部分，是日志的识别信息、日志级别等这些日志信息

	[ERROR]: demo.main_4(line:37) ==> '/Users/zhangyi/DemoCode/PythonToolLib/日志处理/demo.py'
	[日志级别]: 模块名.函数名(line:行号) ==> '程序绝对路径'

第三部分，在 `-` 最后的最后部分，是日志输出的具体内容，内容是我们自定义的，也就是 `logging.error('error')` 里面的 `error`