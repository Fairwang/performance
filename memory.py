# user/bin/env
# -*- coding:utf-8 -*-
import os
import time
class memory(object):
    def __init__(self,count,papename):
        self.count=count
        self.memfile=open("memofile.txt","w")
        self.pagename=papename
#单次测试过程
    def testRunTime(self):
        cmd="adb shell dumpsys meminfo "+self.pagename
        result =os.popen(cmd).readlines()
        for line in result:
            if 'TOTAL' in line:
                mem=line.split("    ")[3]
                print("memory", mem)
                self.memfile.write(mem+"\n")
                break

#多次执行测试过程
    def run(self):
        while self.count>0:
            self.testRunTime()
            self.count=self.count-1
            time.sleep(2)
        self.memfile.close()

count=2
pagename="com.eg.android.AlipayGphone"
if __name__=="__main__":
    controller=memory(count,pagename)
    controller.run()

