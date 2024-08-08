from . import format


def bridge(ai_):
    # 实例化抽象类
    ai = format.format('天桥',ai_)
    # 启动语言
    ai.start()

    while 1:
        # 语言识别
        data = ai.data_()

        # 位置判断
        ai.now_place()

        # 组件汇总
        if ('系统' in data):
            if ('组件' in data):
                ai_.say('天桥现可连接主机：')
                ai_.say('一号主机:神威')
                continue

        #连接一号主机
        ai.app_open_off('1号',r"D:\A_HAT\server_tool\SHENWEI(758790735).lnk",'SHENWEI(758790735).lnk','神威')



        # 关闭系统判断
        if ai.off():
            break