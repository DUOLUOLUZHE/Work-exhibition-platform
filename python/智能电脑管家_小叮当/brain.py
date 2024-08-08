import pyttsx3
import pyaudio
import wave
import whisper
from pydub import AudioSegment
from pydub.effects import normalize
import threading

class brain(object):
    #所有固定变量
    def __init__(self):
        #实时语音识别结果
        self.say_data = ''
        #保存音频名称
        self.name = 'new_wav'
        #保存模型的变量
        #self.model = None
        #关键字词典
        #self.custom_keywords = None
        #初始化语音识别模型
        self.first_thing()
        #启动实例并不断刷新语音识别结果
        t1 = threading.Thread(target=self.start)
        t1.start()

    #实例的运行实体
    def start(self):
        i = 0
        while True:
            #先听
            self.ear()
            print(i)
            i += 1
            # #识别
            self.think()
            # t2 = threading.Thread(target=self.think)
            # t2.start()



    #听到的音频转wav文件
    def ear(self):
        CHUNK = 256
        FORMAT = pyaudio.paInt16
        CHANNELS = 1  # 声道数
        RATE = 11025  # 采样率
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = './' + str(self.name) + '.wav'  # 存储位置
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        # print('开始录音')
        #say('开始录音')
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        # print('开始录音')
        #say('录音结束')

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        # 加载音频文件
        audio = AudioSegment.from_file(str(self.name) + ".wav")

        # 音量标准化
        audio = normalize(audio)

        # 保存预处理后的音频文件
        audio.export("./" + str(self.name) + ".wav", format="wav")

    # 实现音频转化为文本
    # 初始化模型
    def first_thing(self):
        # 加载 Whisper 模型
        self.model = whisper.load_model("medium")
        # ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large']
        # large 超大型模型，准确率极高，但是极其缓慢 推荐大型机器使用
        # medium 中型模型，识别效率不错，速率中等 推荐中小型机器使用
        # small 小型模型，极快，识别极差 推荐老旧设备使用
        # base 微型模型，速度极快，但是几乎无准确率 推荐嵌入式装备使用
        # tiny 垃圾

        # 自定义关键字词典
        self.custom_keywords = ['停止', '继续', '私人', '音乐', '一号', '天桥', '模拟器', '网络分析器', '笔记本', '鲨鱼', '云端', 'VS', '生活', '学者',
                           '计算器', '有道词典', "小叮当", '黑客', '开启', '问个好', 'ip', '端口', '系统', '无线网', '圣所',
                           '物理', '地址', '关闭', 'IP', '生活', '本地', '子域名', '当前', '位置', '组件', '灯塔', '休眠']

    # 使用模型进行转换
    def think(self):

        # 读取音频文件
        audio_file = "./" + str(self.name) + ".wav"

        # 使用 Whisper 模型进行音频转文本
        result = self.model.transcribe(audio_file, language='zh')

        # 结果后处理
        def correct_keywords(text, keywords):
            for keyword in keywords:
                if keyword.lower() in text.lower():
                    text = text.replace(keyword.lower(), keyword)
            return text

        # 获取转录结果文本
        transcription_text = result["text"]

        # 进行关键字纠错
        corrected_text = correct_keywords(transcription_text, self.custom_keywords)
        print(corrected_text)
        self.say_data = corrected_text

    # 实现文本转语音
    def say(self,txt):
        say_windower = pyttsx3.init()
        say_windower.say(txt)
        say_windower.runAndWait()

