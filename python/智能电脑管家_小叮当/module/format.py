#所有模块的通用模版抽象类

import os


class format():
    def __init__(self,name,ai):
        self.name = name
        self.ai = ai

    def start(self):
        self.ai.say('成功启动'+self.name+'模块')

    def data_(self):
        self.data = self.ai.say_data
        return self.data

    def now_place(self):
        if ('当前' in self.data):
            if ('位置' in self.data):
                self.ai.say('当前位置为' + self.name + '系统')

    def app_open_off(self,think,place,app_name,tool_name):
        self.think = think
        self.place = place
        self.app_name = app_name
        self.tool_name = tool_name

        if (self.think in self.data):
            if ('开启' in self.data):
                self.ai.say(self.tool_name+'已就绪')
                os.system(r"start "+ self.place)

            if ('关闭' in self.data):
                os.system(r"taskkill -f -im "+ self.app_name)
                self.ai.say('已关闭'+self.tool_name)


    def off(self):
        if ('关闭' in self.data):
            if (self.name in self.data):
                self.ai.say(self.name + '模块已关闭')
                return 1
            return 0
        return 0





