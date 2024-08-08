#人工智能小叮当所在，管理各个模块入口

import time
#黑客系统
from module import harker
#学者系统
from module import scholar
#侍从系统
from module import live
#通天塔
from module import bridge





def now_time():
    t = time.localtime()
    #当前完整时间
    now = '当前时间'+ str(t.tm_year) +'年'+str(t.tm_mon)+'月'+str(t.tm_mday) +'日' +str(t.tm_hour)+'点' +str(t.tm_min) +'分' +str(t.tm_sec)+'秒'

    if 6 <= int(t.tm_hour) <= 12:
        return now,'上午'
    elif 13 <= int(t.tm_hour) <= 17:
        return now,'下午'
    elif 18 <= int(t.tm_hour) <= 24:
        return now,'晚上'
    elif 0 <= int(t.tm_hour) <= 5:
        return now,'凌晨'

def administrator(ai):

    #提示音
    ai.say('人工智能已激活')
    time.sleep(0.5)
    ai.say('智能管家小叮当为您服务')
    time.sleep(0.1)
    #时间判定
    now,now_plan = now_time()
    ai.say(now)
    ai.say(str(now_plan) + '好，少爷')
    while 1:
        data = ai.say_data
        if('当前' in data):
            if('位置' in data):
                ai.say('当前位置为小叮当管理层')

        if ('问个好' in data):
            ai.say('大家好，我是胡少爷编写的管家型人工智能小叮当，很高兴与大家见面')
            continue

        if ('黑客' in data):
            ai.say('正在启动黑客模块')
            harker.harker(ai)
            continue

        if ('学者' in data):
            ai.say('正在启动学者模块')
            scholar.scholar(ai)
            continue

        if ('天桥' in data):
            ai.say('正在启动天桥')
            bridge.bridge(ai)
            continue

        if ('生活' in data):
            ai.say('正在启动生活模块')
            live.attendants(ai)
            continue

        if ('休眠' in data):
            ai.say('人工智能小叮当已进入休眠')
            break

