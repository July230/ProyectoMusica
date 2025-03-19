from music21 import note, stream, chord

# Nota
# A - La
# B - Si
# C - Do
# D - Re
# E - Mi
# F - Fa
# G - Sol
miNota = note.Note("C")

# funcion que imprime una nota que dura 3 tiempos de negra
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

    # quarterLength = 1 tiempo de negra (default)
    miNota.duration.quarterLength = 3
    print(miNota.duration.quarterLength)

# funcion que imprimer las notas do re y mi siendo mi una blanca
def do_re_mi(unPentagrama):
    do = note.Note('C')
    pentagrama.append(do)

    re = note.Note('D')
    pentagrama.append(re)

    mi = note.Note('E')
    mi.duration.quarterLength = 2
    pentagrama.append(mi)

# funcion que imprimer las notas re y mi
def re_mi(un_pentagrama):
    re = note.Note('D')
    un_pentagrama.append(re)

    mi = note.Note('E')
    un_pentagrama.append(mi)

# funcion que imprimer la nota do
def do(un_pentagrama):
    do = note.Note('C')
    do.duration.quarterLength = 2
    un_pentagrama.append(do)

def miSiMi(unPentagrama):
    mi3 = note.Note('E3')
    mi3.duration.quarterLength = 0.5
    unPentagrama.append(mi3)
    si3 = note.Note('B3')
    si3.duration.quarterLength = 0.5
    unPentagrama.append(si3)
    mi4 = note.Note('E4')
    mi4.duration.quarterLength = 0.5
    unPentagrama.append(mi4)

def miSi3(unPentagrama):
    mi3 = note.Note('E3')
    mi3.duration.quarterLength = 0.5
    unPentagrama.append(mi3)
    si3 = note.Note('B3')
    si3.duration.quarterLength = 0.5
    unPentagrama.append(si3)

def miSi4(unPentagrama):
    mi4 = note.Note('E4')
    mi4.duration.quarterLength = 0.5
    unPentagrama.append(mi4)
    si4 = note.Note('B4')
    si4.duration.quarterLength = 0.5
    unPentagrama.append(si4)

def reDos5(unPentagrama):
    re5 = note.Note('D5')
    re5.duration.quarterLength = 0.5
    unPentagrama.append(re5)
    doSostenido5 = note.Note('C5#')
    doSostenido5.duration.quarterLength = 0.5
    unPentagrama.append(doSostenido5)

# Crear el pentagrama que va a contener las notas de la partitura
pentagrama = stream.Stream()
for i in range(8):
    miSi3(pentagrama)
    miSi4(pentagrama)
miSiMi(pentagrama)
reDos5(pentagrama)


pentagrama.show()

# Abrir el reproductor de midi's con un archivo midi con la nota Do
# miNota.show('midi')