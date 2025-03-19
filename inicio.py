from music21 import note, stream

# Nota
# A - La
# B - Si
# C - Do
# D - Re
# E - Mi
# F - Fa
# G - Sol
miNota = note.Note("C")

def imprimirNota():

    # Abrir el editor de partituras con la nota
    miNota.show()

    print(miNota)
    print(miNota.name)
    print(miNota.octave)
    print(miNota.pitch)
    print(miNota.pitch.frequency)
    print(miNota.pitch.spanish)
    print(miNota.duration.quarterLength)

    miNota.duration.quarterLength = 3
    print(miNota.duration.quarterLength)

do = note.Note('C')
re = note.Note('D')
mi = note.Note('E')

# Crear el pentagrama que va a contener las notas de la partitura
pentagrama = stream.Stream()
pentagrama.append(do)
pentagrama.append(re)
pentagrama.append(mi)
pentagrama.show()

# Abrir el reproductor de midi's con un archivo midi con la nota Do
# miNota.show('midi')