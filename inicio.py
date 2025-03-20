from music21 import note, stream, chord, tempo, clef, instrument

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

def definirTempo(unPentagrama):
    # Crear un objeto de tempo (metronome mark)
    tiempo = tempo.MetronomeMark(number=140)
    tiempo.number
    tiempo.referent
    tiempo.referent.type
    unPentagrama.append(tiempo)
    print(tiempo.text)

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
    unPentagrama.append(mi3)
    si3 = note.Note('B3')
    unPentagrama.append(si3)
    mi4 = note.Note('E4')
    unPentagrama.append(mi4)

def miSi3(unPentagrama):
    mi3 = note.Note('E3')
    unPentagrama.append(mi3)
    si3 = note.Note('B3')
    unPentagrama.append(si3)

def miSi4(unPentagrama):
    mi4 = note.Note('E4')
    unPentagrama.append(mi4)
    si4 = note.Note('B4')
    unPentagrama.append(si4)

def reDos5(unPentagrama):
    re5 = note.Note('D5')
    unPentagrama.append(re5)
    doSostenido5 = note.Note('C5#')
    unPentagrama.append(doSostenido5)

def doMenor(unPentagrama):
    doMenor4 = chord.Chord(["C4", "E-4", "G4"])
    doMenor4.duration.quarterLength = 4
    unPentagrama.append(doMenor4)

# Un silencio o descanso es una nota que no se ejecuta
def silencioDeNegra(unPentagrama):
    silencio = note.Rest()
    unPentagrama.append(silencio)

def escalaDeLa(unPentagrama):
    la3 = note.Note('A3')
    unPentagrama.append(la3)
    si3 = note.Note('B3')
    unPentagrama.append(si3)
    doSostenido4 = note.Note('C#4')
    unPentagrama.append(doSostenido4)
    re4 = note.Note('D4')
    unPentagrama.append(re4)
    mi4 = note.Note('E4')
    unPentagrama.append(mi4)
    faSostenido4 = note.Note('F#4')
    unPentagrama.append(faSostenido4)
    solSostenido4 = note.Note('G#4')
    unPentagrama.append(solSostenido4)
    la4 = note.Note('A4')
    unPentagrama.append(la4)

# cambiar a clave de fa
def claveDeFa(unPentagrama):
    claveFa = clef.FClef()
    unPentagrama.append(claveFa)

# usar la guitarra
def guitarra(unPentagrama):
    unPentagrama.insert(0, instrument.Guitar()) # (intervalo del compas, instrumento)

# Crear el pentagrama que va a contener las notas de la partitura
pentagrama = stream.Stream()
guitarra(pentagrama)
definirTempo(pentagrama)
escalaDeLa(pentagrama)
claveDeFa(pentagrama)
escalaDeLa(pentagrama)

pentagrama.show()

# Abrir el reproductor de midi's con un archivo midi con la nota Do
# miNota.show('midi')