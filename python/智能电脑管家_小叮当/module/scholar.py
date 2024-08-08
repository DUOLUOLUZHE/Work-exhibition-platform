from . import format

def scholar(ai_):
    #实例化抽象类
    ai = format.format('学者',ai_)
    #启动语言
    ai.start()

    while 1:
        #语言识别
        data = ai.data_()

        #位置判断
        ai.now_place()

        # 组件汇总
        if ('系统' in data):
            if ('组件' in data):
                ai_.say('学者系统现有的组件有:')
                ai_.say('计算器')
                ai_.say('网易有道词典')
                ai_.say('VS')
                ai_.say('笔记本')
                continue


        #计算器操控
        ai.app_open_off('计算器',r'C:\Windows\System32\calc.exe','calc.exe','计算器')

        # 网易有道词典操控
        ai.app_open_off('有道词典',r'C:\Users\胡冬阳\AppData\Local\youdao\dict\Application\YoudaoDict.exe', 'YoudaoDict.exe','网易有道词典')

        # VS操控
        ai.app_open_off('VS', r"D:\A_HAT\C\VS\VS\Common7\IDE\devenv.exe", 'devenv.exe','Visual Studio 2019')

        # 笔记本
        ai.app_open_off('笔记', r'D:\A_HAT\notebook\ediary\eDiary\eDiary\eDiary.exe', 'eDiary.exe','笔记本')




        #关闭系统判断
        if ai.off():
            break




