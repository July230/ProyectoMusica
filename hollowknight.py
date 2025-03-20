"""
Ian Julián Estrada Castro 
"""

from music21 import note, stream, chord, tempo, clef, meter, instrument

def definirTempo(unPentagrama):
    # Crear un objeto de tempo (metronome mark)
    tiempo = tempo.MetronomeMark(number=120)
    tiempo.number
    tiempo.referent
    tiempo.referent.type
    unPentagrama.append(tiempo)
    print(tiempo.text)

def do4Sol4Lab4(unPentagrama):
    do4 = note.Note("C")
    do4.duration.quarterLength = 0.5
    unPentagrama.append(do4)



# Crear la partitura
partitura = stream.Score()

# Crear primer pentagrama que va a contener la armonia
pentagrama1 = stream.Part()

# Crear segundo pentagrama que va a contener la melodia
pentagrama2 = stream.Part()

partitura.append(pentagrama2)
partitura.append(pentagrama1)
partitura.show()

# Crear y escribir la cancion
# partitura.write('midi', 'hollowknight.mid')
