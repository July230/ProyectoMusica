from music21 import note, stream, chord, tempo, clef, meter, instrument

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
    tiempo = tempo.MetronomeMark(number=120)
    tiempo.number
    tiempo.referent
    tiempo.referent.type
    unPentagrama.append(tiempo)
    print(tiempo.text)

def doMenor(unPentagrama):
    doMenor4 = chord.Chord(["C4", "E-4", "G4"])
    doMenor4.duration.quarterLength = 4
    unPentagrama.append(doMenor4)

# Un silencio o descanso es una nota que no se ejecuta
def silencioDeNegra(unPentagrama):
    silencio = note.Rest()
    unPentagrama.append(silencio)

def silencioDeBlancoYMedio(unPentagrama):
    silencio = note.Rest()
    silencio.duration.quarterLength = 3
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

# cambiar a clave de sol
def claveDeSol(unPentagrama):
    claveSol = clef.GClef()
    unPentagrama.append(claveSol)

# usar la guitarra
def guitarra(unPentagrama):
    unPentagrama.insert(0, instrument.Guitar()) # (intervalo del compas, instrumento)

def piano(unPentagrama):
    unPentagrama.insert(0, instrument.Piano())

def tiempoTresCuartos(unPentagrama):
    tiempoTresCuartos = meter.TimeSignature("3/4")
    unPentagrama.append(tiempoTresCuartos)

def laMi(unPentagrama):
    la2 = note.Note('A2')
    la2.duration.quarterLength = 0.5
    unPentagrama.append(la2)
    mi2 = note.Note('E3')
    mi2.duration.quarterLength = 0.5
    unPentagrama.append(mi2)

def siDoYFa(unPentagrama):
    siDoYFA = chord.Chord(["A3", "C4", "F4"])
    siDoYFA.duration.quarterLength = 0.5
    unPentagrama.append(siDoYFA)

def doYFa(unPentagrama):
    doYFA = chord.Chord(["C4", "F4"])
    doYFA.duration.quarterLength = 0.5
    unPentagrama.append(doYFA)

def reYSol(unPentagrama):
    reYSol = chord.Chord(["D4", "G4"])
    reYSol.duration.quarterLength = 0.5
    unPentagrama.append(reYSol)

def laDoYFa(unPentagrama):
    laDoYFa = chord.Chord(["A2", "C4", "F4"])
    laDoYFa.duration.quarterLength = 0.5
    unPentagrama.append(laDoYFa)

def laReYSol(unPentagrama):
    laReYSol = chord.Chord(["A2", "D4", "G4"])
    laReYSol.duration.quarterLength = 0.5
    unPentagrama.append(laReYSol)

def la3DoYFa(unPentagrama):
    la3DoYFa = chord.Chord(["A3", "C4", "F4"])
    la3DoYFa.duration.quarterLength = 0.5
    unPentagrama.append(la3DoYFa)

def siYMi(unPentagrama):
    siYMi = chord.Chord(["E3", "B3"])
    siYMi.duration.quarterLength = 0.5
    unPentagrama.append(siYMi)

def doYMi(unPentagrama):
    doYMi = chord.Chord(["E3", "C4"])
    doYMi.duration.quarterLength = 0.5
    unPentagrama.append(doYMi)

def si(unPentagrama):
    si3 = note.Note('B3')
    si3.duration.quarterLength = 0.5
    unPentagrama.append(si3)

def do(unPentagrama):
    do4 = note.Note('C4')
    do4.duration.quarterLength = 0.5
    unPentagrama.append(do4)

def miOctavado(unPentagrama):
    miOctavado = chord.Chord(["E5", "E6"])
    unPentagrama.append(miOctavado)

def reOctavado(unPentagrama):
    reOctavado = chord.Chord(["D5", "D6"])
    unPentagrama.append(reOctavado)

def laOctavadoTresTiempos(unPentagrama):
    laOctavadoTresTiempos = chord.Chord(["A4", "A5"])
    laOctavadoTresTiempos.duration.quarterLength = 3
    unPentagrama.append(laOctavadoTresTiempos)

def solOctavadoDosTiempos(unPentagrama):
    laOctavado = chord.Chord(["G5", "G6"])
    laOctavado.duration.quarterLength = 2
    unPentagrama.append(laOctavado)

def faOctavado(unPentagrama):
    faOctavado = chord.Chord(["F5", "F6"])
    unPentagrama.append(faOctavado)

def miOctavadoTresTiempos(unPentagrama):
    miOctavadoTresTiempos = chord.Chord(["E5", "E6"])
    miOctavadoTresTiempos.duration.quarterLength = 3
    unPentagrama.append(miOctavadoTresTiempos)


# Crear la partitura
partitura = stream.Score()

# Crear primer pentagrama que va a contener las notas de la partitura (Clave de Fa, para guitarra)

pentagrama1 = stream.Part()
claveDeFa(pentagrama1)
tiempoTresCuartos(pentagrama1)
definirTempo(pentagrama1)
piano(pentagrama1)
laMi(pentagrama1)
siDoYFa(pentagrama1)
si(pentagrama1)
doYFa(pentagrama1)
si(pentagrama1)
laDoYFa(pentagrama1)
siYMi(pentagrama1)
la3DoYFa(pentagrama1)
si(pentagrama1)
doYFa(pentagrama1)
si(pentagrama1)
for i in range(2):
    laDoYFa(pentagrama1)
    siYMi(pentagrama1)
    la3DoYFa(pentagrama1)
    si(pentagrama1)
    doYFa(pentagrama1)
    si(pentagrama1)

for i in range(4):
    laReYSol(pentagrama1)
    doYMi(pentagrama1)
    reYSol(pentagrama1)
    do(pentagrama1)
    reYSol(pentagrama1)
    do(pentagrama1)

laMi(pentagrama1)
siDoYFa(pentagrama1)
si(pentagrama1)
doYFa(pentagrama1)
si(pentagrama1)
laDoYFa(pentagrama1)
siYMi(pentagrama1)
la3DoYFa(pentagrama1)
si(pentagrama1)
doYFa(pentagrama1)
si(pentagrama1)

# Crear segundo pentagrama
pentagrama2 = stream.Part()
claveDeSol(pentagrama2)
tiempoTresCuartos(pentagrama2)
definirTempo(pentagrama1)
piano(pentagrama2)
silencioDeNegra(pentagrama2)
miOctavado(pentagrama2)
reOctavado(pentagrama2)
laOctavadoTresTiempos(pentagrama2)
silencioDeNegra(pentagrama2)
miOctavado(pentagrama2)
reOctavado(pentagrama2)
solOctavadoDosTiempos(pentagrama2)
faOctavado(pentagrama2)
miOctavadoTresTiempos(pentagrama2)
silencioDeBlancoYMedio(pentagrama2)
silencioDeBlancoYMedio(pentagrama2)
silencioDeBlancoYMedio(pentagrama2)
silencioDeNegra(pentagrama2)
miOctavado(pentagrama2)
reOctavado(pentagrama2)
laOctavadoTresTiempos(pentagrama2)


partitura.append(pentagrama2)
partitura.append(pentagrama1)
partitura.show()

# Abrir el reproductor de midi's con un archivo midi con la nota Do
# miNota.show('midi')