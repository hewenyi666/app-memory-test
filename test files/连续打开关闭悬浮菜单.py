#打开关闭悬浮菜单 10次
from uiautomator import Device
import time
d=Device('04110258C5000088')
time.sleep(1)
d(resourceId='com.hanvon.xpen:id/img_painting').click()
time.sleep(0.5)
with open(r'../data/start-xuanfu.txt','w') as file2:
    file2.write('11')
for i in range(10):
     d.click(1072,1760)
     time.sleep(1)
     d.click(949,1070)
     time.sleep(1)
with open(r'../data/stop-xuanfu.txt','w',encoding='utf-8') as fff:
     fff.write('stop')
print('OK')



