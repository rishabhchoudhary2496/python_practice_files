import os
from player import Player
from random import shuffle
from time import sleep


class Init:
    file_extensions = ['.mp3','.wav','.mp4','.aac']
    music_files_path = []


    def __init__(self,rootPath) -> None:
        self.rootPath = rootPath
    

    def walkDirectory(self):
        music_count = 0
        for root,dir,files in os.walk(self.rootPath):
            for file in files:
                file_path = os.path.join(root,file)
                filename,extension = os.path.splitext(file)
                if extension not in Init.file_extensions:
                    continue
                Init.music_files_path.append(file_path)
                music_count += 1
    
        print('music files found ',music_count)
                       

    def shuffleList(self):
        shuffle(Init.music_files_path)



init = Init("D:\\Music") #root folder where music is
init.walkDirectory()
init.shuffleList()

for song  in Init.music_files_path:
    music_player = Player(song)
    music_player.play() 
    #let wait for 30 sec and pause and play agian
    sleep(10)
    music_player.pause()




