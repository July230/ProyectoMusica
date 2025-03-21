"""
Ian Julián Estrada Castro 
"""
from pygame import mixer
import time

# inicializar el mixer
mixer.init()

# cargar el archivo midi
mixer.music.load('gwyn.mid')

# reproducir archivo midi dos veces
mixer.music.play(2)

while True:
    time.sleep(0.1)