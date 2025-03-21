"""
Ian Julián Estrada Castro 
"""

from music21 import note, stream, chord, tempo, clef, meter, instrument, spanner

def piano(unPentagrama):
    unPentagrama.insert(0, instrument.Piano())

def compasTresCuartos(unPentagrama):
    tiempoTresCuartos = meter.TimeSignature("3/4")
    unPentagrama.append(tiempoTresCuartos)

def definirTempo(unPentagrama):
    # Crear un objeto de tempo (metronome mark)
    tiempo = tempo.MetronomeMark(number=55)
    tiempo.number
    tiempo.referent
    tiempo.referent.type
    unPentagrama.append(tiempo)
    print(tiempo.text)

# cambiar a clave de fa
def claveDeFa(unPentagrama):
    claveFa = clef.FClef()
    unPentagrama.append(claveFa)

# cambiar a clave de sol
def claveDeSol(unPentagrama):
    claveSol = clef.GClef()
    unPentagrama.append(claveSol)

def silencioDeBlancoYMedio(unPentagrama):
    silencio = note.Rest()
    silencio.duration.quarterLength = 3
    unPentagrama.append(silencio)

# notas solas
def do5Negra(unPentagrama):
    do5 = note.Note("C5")
    unPentagrama.append(do5)

def do5BlancaYPunto(unPentagrama):
    do5 = note.Note("C5")
    do5.duration.quarterLength = 3
    unPentagrama.append(do5)

def solSostenido4Negra(unPentagrama):
    solSostenido4 = note.Note("G#4")
    unPentagrama.append(solSostenido4)

def re5BlancaYPunto(unPentagrama):
    re5 = note.Note("D5")
    re5.duration.quarterLength = 3
    unPentagrama.append(re5)

def sol4BlancaYPunto(unPentagrama):
    sol4 = note.Note("G4")
    sol4.duration.quarterLength = 3
    unPentagrama.append(sol4)

def fa5BlancaYPunto(unPentagrama):
    fa5 = note.Note("F5")
    fa5.duration.quarterLength = 3
    unPentagrama.append(fa5)

def fa4Blanca(unPentagrama):
    fa4 = note.Note("F4")
    fa4.duration.quarterLength = 2
    unPentagrama.append(fa4)

def do5Corchea(unPentagrama):
    do5 = note.Note("C5")
    do5.duration.quarterLength = 0.5
    unPentagrama.append(do5)

def mib4Corchea(unPentagrama):
    mib4 = note.Note("E-4")
    mib4.duration.quarterLength = 0.5
    unPentagrama.append(mib4)

def sol4Corchea(unPentagrama):
    sol4 = note.Note("G4")
    sol4.duration.quarterLength = 0.5
    unPentagrama.append(sol4)

def fa4Corchea(unPentagrama):
    fa4 = note.Note("F4")
    fa4.duration.quarterLength = 0.5
    unPentagrama.append(fa4)

def sib3Corchea(unPentagrama):
    sib3 = note.Note("B-3")
    sib3.duration.quarterLength = 0.5
    unPentagrama.append(sib3)

def lab3Corchea(unPentagrama):
    lab3 = note.Note("A-3")
    lab3.duration.quarterLength = 0.5
    unPentagrama.append(lab3)


# armonias
def re5Mib5Corcheas(unPentagrama):
    re5 = note.Note("D5")
    re5.duration.quarterLength = 0.5
    unPentagrama.append(re5)

    mib5 = note.Note("E-5")
    mib5.duration.quarterLength = 0.5
    unPentagrama.append(mib5)


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

def do4Mib4Fa4(unPentagrama):
    do4 = note.Note("C")
    do4.duration.quarterLength = 0.5
    unPentagrama.append(do4)

    mib4 = note.Note("E-4")
    mib4.duration.quarterLength = 0.5
    unPentagrama.append(mib4)

    Fa4 = note.Note("F4")
    Fa4.duration.quarterLength = 2
    unPentagrama.append(Fa4)

def do4Mib4Fa4(unPentagrama):
    do4 = note.Note("C")
    do4.duration.quarterLength = 0.5
    unPentagrama.append(do4)

    mib4 = note.Note("E-4")
    mib4.duration.quarterLength = 0.5
    unPentagrama.append(mib4)

    fa4 = note.Note("F4")
    fa4.duration.quarterLength = 2
    unPentagrama.append(fa4)

def do4Re4Mib4Re4Sib3(unPentagrama):
    do4 = note.Note("C")
    do4.duration.quarterLength = 0.5
    unPentagrama.append(do4)

    re4 = note.Note("D4")
    re4.duration.quarterLength = 0.5
    unPentagrama.append(re4)

    mib4 = note.Note("E-4")
    mib4.duration.quarterLength = 0.5
    unPentagrama.append(mib4)

    re4 = note.Note("D4")
    re4.duration.quarterLength = 0.5
    unPentagrama.append(re4)

    sib3 = note.Note("B-3")
    sib3.duration.quarterLength = 1
    unPentagrama.append(sib3)

def fa3Sib3Do4Fa4Do4Sib3(unPentagrama):
    fa3 = note.Note("F3")
    fa3.duration.quarterLength = 0.5
    unPentagrama.append(fa3)

    sib3 = note.Note("B-3")
    sib3.duration.quarterLength = 0.5
    unPentagrama.append(sib3)

    do4 = note.Note("C")
    do4.duration.quarterLength = 0.5
    unPentagrama.append(do4)

    fa4 = note.Note("F4")
    fa4.duration.quarterLength = 0.5
    unPentagrama.append(fa4)

    do4_2 = note.Note("C")
    do4_2.duration.quarterLength = 0.5
    unPentagrama.append(do4_2)

    sib3_2 = note.Note("B-3")
    sib3_2.duration.quarterLength = 0.5
    unPentagrama.append(sib3_2)

def sol5Mib5Re5Do5Sib4(unPentagrama):
    sol5 = note.Note("G5")
    sol5.duration.quarterLength = 0.5
    unPentagrama.append(sol5)

    mib5 = note.Note("E-5")
    mib5.duration.quarterLength = 0.5
    unPentagrama.append(mib5)

    re5 = note.Note("D5")
    re5.duration.quarterLength = 0.5
    unPentagrama.append(re5)

    do5 = note.Note("C5")
    do5.duration.quarterLength = 0.5
    unPentagrama.append(do5)

    sib4 = note.Note("B-4")
    sib4.duration.quarterLength = 1
    unPentagrama.append(sib4)


# Crear la partitura
partitura = stream.Score()

# Crear primer pentagrama que va a contener la armonia
# mano derecha
pentagrama1 = stream.Part()
compasTresCuartos(pentagrama1)
definirTempo(pentagrama1)
for i in range(2):
    do5Negra(pentagrama1)
re5Mib5Corcheas(pentagrama1)
re5BlancaYPunto(pentagrama1)
do5Corchea(pentagrama1)
sol4Corchea(pentagrama1)
solSostenido4Negra(pentagrama1)
sol4Corchea(pentagrama1)
fa4Corchea(pentagrama1)
sol4BlancaYPunto(pentagrama1)
for i in range(2):
    do5Negra(pentagrama1)
re5Mib5Corcheas(pentagrama1)
fa5BlancaYPunto(pentagrama1)
sol5Mib5Re5Do5Sib4(pentagrama1)
do5BlancaYPunto(pentagrama1)

# Crear segundo pentagrama que va a contener la melodia
# mano izquierda
pentagrama2 = stream.Part()
compasTresCuartos(pentagrama2)
definirTempo(pentagrama2)
do4Sol4Lab4(pentagrama2)
do4Fa4Sol4(pentagrama2)
do4Mib4Fa4(pentagrama2)
do4Re4Mib4Re4Sib3(pentagrama2)
do4Sol4Lab4(pentagrama2)
sib3Corchea(pentagrama2)
sol4Corchea(pentagrama2)
fa4Blanca(pentagrama2)
lab3Corchea(pentagrama2)
mib4Corchea(pentagrama2)
fa4Blanca(pentagrama2)
fa3Sib3Do4Fa4Do4Sib3(pentagrama2)



partitura.append(pentagrama1)
partitura.append(pentagrama2)
partitura.show()

# Crear y escribir la cancion
# partitura.write('midi', 'hollowknight.mid')
