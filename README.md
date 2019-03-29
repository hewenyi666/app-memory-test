                                             # app-memory-test
                                             监控app内存的脚本(python)
  目前该工具包括3个文件夹,data,memory result和test files.test files文件夹存放测试脚本,包括4个app自动化测试脚本和1个内存测试脚本(record memory.py)  
app主要使用了uiautomator这个测试框架,内存测试脚本是基于adb shell dumpsys meminfo命令,测试当前app的内存占用.memory result文件夹中存放测试结果,一个excel表,一个html格式的图表(有柱形图和折线图2种形态).data文件夹用于存放启动,结束的判断文件  
    使用方法:1.使用前先清空data,memory result文件夹中的所有文件
          2.打开test files中的record memory.py文件
          3.修改record memory.py中filename和filename1的文件名,这两个文件是用于判断内存记录脚本启动和结束,想要记录哪个脚本的内存,将filename
          和filename1分别改为各测试脚本生成的文件名即可,如分别改为start-note,stop-note,start-memo,stop-memo等
          4.运行测试脚本,每个测试脚本中都加入了新建文件(用于给record memory.py的启动和结束提供判断),如start-note,stop-note等文件
          
    备注:https://github.com/xiaocong/uiautomator,这是学习uiautomator的网址
  
    存在的不足及优化方向:
            1.使用前得先运行内存测试脚本,再运行自动化测试脚本,是否可以使用多线程,将2个功能合二为一?
            2.未加入日志记录功能
            3.可以加入文件判断,不用重复新建,删除data中的文件,使用更便捷
            4.生成的html格式图表使用了pyecharts这个库,是否换成其他库,生成更美观的图表?
            5.目前只能单独测试一个脚本的内存,未使用类似批量执行的功能,如使用unittest,pytest批量执行测试脚本,然后自动生成各脚本的内存占用情况
            6.目前使用内存测试脚本前,需要编辑脚本,修改filename和filename1的文件名的文件名称,可以单独在该文件夹中创建一个文件,filename和filename1        的内容直接从该文件中读取,这样修改更便捷,不容易出错!
           
