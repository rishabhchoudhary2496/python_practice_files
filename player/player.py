from pygame import mixer
import pygame

class Player:
    def __init__(self,track) -> None:
        self.track = track
        mixer.init()
        mixer.music.load(self.track)

    def play(self):
        mixer.music.play()
        print("Now playing",self.track)
        while mixer.music.get_busy(): 
            continue

    def pause(self):
        mixer.music.pause()

    def stop(self):
        mixer.music.stop()


if __name__ == '___main__':
    mixer.init() #Initialzing pyamge mixer

    mixer.music.load('weather_report-3512872.mp3') #Loading Music File

    mixer.music.play() #Playing Music with Pygame
