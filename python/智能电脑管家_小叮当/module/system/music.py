import pygame
pygame.mixer.init()
import threading
import random
import os


class music(object):
    def __init__(self):
        self.one_delete = False
        self.open_off = 1

    def open(self):
        pygame.mixer.music.unpause()  # 取消暂停

    def stop(self):
        pygame.mixer.music.pause()  # 暂停


    def run(self,name):
        if name == '私人':
            self.name = name
            name_list = os.listdir(r'E:\music_database\私人')
            random.shuffle(name_list)
            for one_name in name_list:
                track = pygame.mixer.music.load(r'E:\music_database\私人\\' + str(one_name))
                pygame.mixer.music.play()


                # while 1:
                #     data = ai.data_(model, custom_keywords,'attendats_music')
                #     if self.open_off == 1:
                #         t1 = threading.Thread(target=self.run_music,args=(one_name,name,))
                #         t1.start()
                #         self.open_off = 0
                #
                #     if self.open_off == 2:
                #         break
                #
                #     if ('下一个' in data):
                #         del t1
                #         self.open_off = 1
                #         break

        elif name == '随机':
            self.name = name
            name_list = os.listdir(r'E:\music_database\随机')
            random.shuffle(name_list)
            for one_name in name_list:
                track = pygame.mixer.music.load(r'E:\music_database\随机\\' + str(one_name))
                pygame.mixer.music.play()

                # while 1:
                #     data = ai.data_(model, custom_keywords, 'attendats_music')
                #     if self.open_off == 1:
                #         t1 = threading.Thread(target=self.run_music, args=(one_name,name,))
                #         t1.start()
                #         self.open_off = 0
                #
                #     if self.open_off == 2:
                #         break
                #
                #     if ('下一个' in data):
                #         del t1
                #         self.open_off = 1
                #         break






