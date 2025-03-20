"""
Ian Julián Estrada Castro 
"""
from pygame import mixer
import time

mixer.init()
mixer.music.load('gwyn.mid')

mixer.music.play(2)

while True:
    time.sleep(0.1)