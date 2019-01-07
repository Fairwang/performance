# user/bin/env
# -*- coding : utf-8 -*-
import os
import time
class cpu(object):
    def __init__(self,count,pagename):
        self.count=count
        self.file=open("cpu.txt",'w')
        self.pagename=pagename

    def testRunTime(self):
        result=os.popen("adb shell dumpsys cpuinfo | findstr "+self.pagename).readlines()
        cputotle=0
        for line in result:
            if len(line)>0:
                cpu=line.split("%")[0].strip()
                if len(cpu)>0:
                    cputotle=cputotle+float(cpu)
                    self.file.write(str(cputotle)+"\n")
    def run(self):
        while self.count>0:
            self.testRunTime()
            self.count=self.count-1
            time.sleep(2)

        self.file.close()

counts=5
pagename="com.eg.android.AlipayGphone"
if __name__=="__main__":
    contorller=cpu(counts,pagename)
    contorller.run()
