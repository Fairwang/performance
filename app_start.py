#!user/bin/env
#  -*-coding: utf-8-*-

#获取APP启动时间
import time ,os
class App():
    def __init__(self,pagename,firstActivity):
        self.pagename=pagename
        self.firstActivty=firstActivity
        self.content=""#执行命令的文本
        self.startTime=""

    def startApp(self):
        cmd="adb shell am start -W -n "+self.pagename+"/"+self.firstActivty
        self.content=os.popen(cmd)

    def stopApp(self):
        cmd="adb shell am force-stop "+self.pagename
        os.popen(cmd)
        print "hh"

    def getStartTime(self):
        for line in  self.content.readlines():
            if "ThisTime" in line:
                self.startTime=line.split(":")[1]
                break
        return self.startTime
# adb =os.popen("adb shell am start -W -n com.eg.android.AlipayGphone/com.eg.android.AlipayGphone.AlipayLogin ")
# adb=os.popen("adb shell am force-stop com.eg.android.AlipayGphone")