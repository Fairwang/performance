#!user/bin/env
# -*-coding : utf-8 -*-
from performance.app import App
import time
import os
class Manager():
    def __init__(self,count,App):
        self.count =count
        self.app=App
        self.file=open("starttime.txt","w")

    def run(self):
        while self.count>0:
            self.app.startApp()
            time.sleep(2)
            self.file.write(self.app.getStartTime())

            time.sleep(2)
            self.app.stopApp()
            print "stop"
            time.sleep(2)
            self.count=self.count-1
            time.sleep(2)

        self.file.close()

# adb =os.popen("adb shell am start -W -n com.eg.android.AlipayGphone/com.eg.android.AlipayGphone.AlipayLogin ")

app=App("com.eg.android.AlipayGphone","com.eg.android.AlipayGphone.AlipayLogin")
m=Manager(3,app)
m.run()
