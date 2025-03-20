"""
Ian Julián Estrada Castro 
"""

from music21 import note, stream, chord, tempo, clef, meter, instrument

def definirTempo(unPentagrama):
    # Crear un objeto de tempo (metronome mark)
    tiempo = tempo.MetronomeMark(number=55)
    tiempo.number
    tiempo.referent
    tiempo.referent.type
    unPentagrama.append(tiempo)
    print(tiempo.text)

def do4Sol4Lab4(unPentagrama):
    do4 = note.Note("C")
    do4.duration.quarterLength = 0.5
    unPentagrama.append(do4)

    sol4 = note.Note("G4")
    sol4.duration.quarterLength = 0.5
    unPentagrama.append(sol4)

    lab4 = note.Note("A-4")
    lab4.duration.quarterLength = 2
    unPentagrama.append(lab4)

def do4Fa4Sol4(unPentagrama):
    do4 = note.Note("C")
    do4.duration.quarterLength = 0.5
    unPentagrama.append(do4)

    Fa4 = note.Note("F4")
    Fa4.duration.quarterLength = 0.5
    unPentagrama.append(Fa4)

    sol4 = note.Note("G4")
    sol4.duration.quarterLength = 2
    unPentagrama.append(sol4)

def do4Fa4Sol4(unPentagrama):
    do4 = note.Note("C")
    do4.duration.quarterLength = 0.5
    unPentagrama.append(do4)

    mib4 = note.Note("E-4")
    mib4.duration.quarterLength = 0.5
    unPentagrama.append(mib4)

    Fa4 = note.Note("F4")
    Fa4.duration.quarterLength = 2
    unPentagrama.append(Fa4)



# Crear la partitura
partitura = stream.Score()

# Crear primer pentagrama que va a contener la armonia
pentagrama1 = stream.Part()
definirTempo(pentagrama1)

# Crear segundo pentagrama que va a contener la melodia
pentagrama2 = stream.Part()
definirTempo(pentagrama2)
do4Sol4Lab4(pentagrama2)
do4Fa4Sol4(pentagrama2)

partitura.append(pentagrama2)
partitura.append(pentagrama1)
partitura.show()

# Crear y escribir la cancion
# partitura.write('midi', 'hollowknight.mid')
