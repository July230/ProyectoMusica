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
fa = 'Notas/fa.mid'
sol = 'Notas/sol.mid'
la = 'Notas/la.mid'
si = 'Notas/si.mid'
do5 = 'Notas/do5.mid'

notas = "asdfghjk"

#while True:
    #tecla = input()

def escalaDeDo(): 
    for tecla in notas:
        if tecla == 'a':
            mixer.music.load(do)
            mixer.music.play()
        if tecla == 's':
            mixer.music.load(re)
            mixer.music.play()
        if tecla == 'd':
            mixer.music.load(mi)
            mixer.music.play()
        if tecla == 'f':
            mixer.music.load(fa)
            mixer.music.play()
        if tecla == 'g':
            mixer.music.load(sol)
            mixer.music.play()
        if tecla == 'h':
            mixer.music.load(la)
            mixer.music.play()
        if tecla == 'j':
            mixer.music.load(si)
            mixer.music.play()
        if tecla == 'k':
            mixer.music.load(do5)
            mixer.music.play()
        time.sleep(0.5)
    
escalaDeDo()