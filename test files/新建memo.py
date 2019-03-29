#新建memo 10次
from uiautomator import Device
import os
import time
d=Device('序列号')#通过adb devices获取序列号
os.popen('activity')#将activity换为要测试界面的activity
time.sleep(1)
d(resourceId='id名称').click()#id名称通过uiautomatorviewer获取
time.sleep(0.5)
with open(r'../data/start-memo.txt','w') as file2:
    file2.write('11')
time1=time.time()
for i in range(10):
     print('正在进行第%d次测试' % (i + 1))
     d(resourceId='id名称').click()
     time.sleep(1)
     d(resourceId='id名称').click()#点击确定
     time.sleep(1)
     d(resourceId='id名称').click()
time2 = time.time()
worktime=time2-time1
with open(r'../data/stop-memo.txt','w',encoding='utf-8') as fff:
     fff.write('stop')
print('共进行了10次测试,所用时间为%ds' % (int(worktime)))



