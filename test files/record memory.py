import subprocess
import re
import time
import xlsxwriter
import os
import xlrd
from pyecharts import Bar
import numpy as np
def get_men(pkg_name, devices):
    try:
        cmd = "adb -s " +  devices +" shell  dumpsys  meminfo %s" % (pkg_name)
        output = subprocess.check_output(cmd,shell=True).split()
        s_men = ".".join([x.decode() for x in output]) # 转换为string
        men2 = int(re.findall("TOTAL.(\d+)*", s_men, re.S)[0])
    except:
        men2 = 0
    return men2
memory=[]
filename='../data/start-painting.txt'
filename1='../data/stop-painting.txt'
while True:
    if os.path.exists(filename) == True:
        memory.append(get_men('包名', '序列号')/1000.0)#包名换为要测试app的报名,序列号通过adb devices获得
        time.sleep(0.1)
    if os.path.exists(filename1) == True:
        break
book=xlsxwriter.Workbook('../memory result/memory.xlsx')
sheet=book.add_worksheet('内存信息')
#sheet.write('A1','memory')
sheet.write_column('A1',memory)
book.close()
data = xlrd.open_workbook(r'../memory result/memory.xlsx')
table = data.sheets()[0]
y=''
#将列的值存入字符串
y=table.col_values(0)#读取列的值
t=np.linspace(1,1000,len(y))#等间隔取值
bar=Bar("app内存统计","单位是M")#主副标题
bar.add("折线图展示",t,y,is_more_utils=True)#标题
bar.render("../memory result/memory chart.html")
