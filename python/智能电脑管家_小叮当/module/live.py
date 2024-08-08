import threading
from . import format
from .system import music

def attendants(ai_):
    # 实例化抽象类
    ai = format.format('生活',ai_)
    # 启动语言
    ai.start()

    #音乐系统的PV开关
    open_off = 1

    while 1:
        # 语言识别
        data = ai.data_()

        # 位置判断
        ai.now_place()

        # 组件汇总
        if ('系统' in data):
            if ('组件' in data):
                ai_.say('侍从系统现有组件：')
                ai_.say('音乐系统')
                continue

        #音乐系统

        if ('音乐' in data):
            if ('系统' in data):
                if  (('开启' in data) and open_off):
                    ai_.say('请指定播放歌单')
                    while 1:
                        data = ai_.say_data
                        if ('当前' in data):
                            if('位置' in data):
                                ai_.say('当前位置为侍从模块下属音乐系统中')

                        if ('私人' in data):
                            one_threading = music.music()
                            t1 = threading.Thread(target=one_threading.run,args=('私人',))
                            t1.start()
                            ai_.say('已为您播放私人歌单音乐')
                            open_off = 0
                            break

                        if ('随机' in data):
                            one_threading = music.music()
                            t1 = threading.Thread(target=one_threading.run,args=('随机',))
                            t1.start()
                            ai_.say('已为您播放随机歌单音乐')
                            open_off = 0
                            break
                elif (('开启' in data) or open_off):
                    ai_.say('当前正在播放私人歌单音乐，无法同时播放多个歌单音乐')


                if (('停止' in data) and (open_off == 0)):
                    try:
                        one_threading.stop()
                        ai_.say('已为您停止音乐播放')
                    except:
                        pass


                if (('继续' in data )and (open_off == 0) ):
                    try:
                        one_threading.open()
                        ai_.say('已为您继续播放音乐')
                    except:
                        pass

                continue




        # 关闭系统判断
        if ai.off():
            break