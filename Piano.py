"""
Ian Julián Estrada Castro 
"""
from pygame import mixer
import time

# inicializar el mixer
mixer.init()

# cargar los archivos midi
do = 'Notas/do.mid'
re = 'Notas/re.mid'
mi = 'Notas/mi.mid'

notas = "asdasdasdsasdsadsada"

while True:
    tecla = input()
#for tecla in notas:
    if tecla == 'a':
        mixer.music.load(do)
        mixer.music.play()
    if tecla == 's':
        mixer.music.load(re)
        mixer.music.play()
    if tecla == 'd':
        mixer.music.load(mi)
        mixer.music.play()
    # time.sleep(0.8)
    