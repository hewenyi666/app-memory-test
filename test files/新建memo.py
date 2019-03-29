#新建memo 10次
from uiautomator import Device
import os
import time
d=Device('04110258C5000088')
os.popen('adb shell am start -n com.hanvon.xpen/com.hanvon.xboard.activities.HistoryAty')
time.sleep(1)
d(resourceId='com.hanvon.xpen:id/img_memo').click()
time.sleep(0.5)
with open(r'../data/start-memo.txt','w') as file2:
    file2.write('11')
time1=time.time()
for i in range(10):
     print('正在进行第%d次测试' % (i + 1))
     d(resourceId='com.hanvon.xpen:id/text_create').click()
     time.sleep(1)
     d(resourceId='com.hanvon.xpen:id/ai_lansel_ok_tv').click()#点击确定
     time.sleep(1)
     d(resourceId='com.hanvon.xpen:id/memo_close').click()
time2 = time.time()
worktime=time2-time1
with open(r'../data/stop-memo.txt','w',encoding='utf-8') as fff:
     fff.write('stop')
print('共进行了10次测试,所用时间为%ds' % (int(worktime)))



