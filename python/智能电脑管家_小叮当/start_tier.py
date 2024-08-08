#这是系统的第一层，目的是做好一切前置准备，并负责唤醒人工智能的小叮当人格

import brain
import admin_tier

if __name__ == '__main__':
    #创建小叮当brain实例
    ai = brain.brain()

    while(1):
        #将实时录音结果提取出来
        data = ai.say_data
        if(('小叮当' in data) or ('小鈴鐺' in data) or ('小叮噹' in data)):
            admin_tier.administrator(ai)

        if('关闭' in data):
            if('系统' in data):
                 ai.say('系统已关闭')
                 break

