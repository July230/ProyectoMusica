from music21 import note, stream, chord

pentagrama = stream.Score()
derecha = stream.Part()
izquierda = stream.Part()


def primera_melodia_izquierda(mi_izquierda):
    n1i = note.Note("A3") # La
    n1i.duration.quarterLength = .75
    mi_izquierda.append(n1i) #.75
    
    n2i = chord.Chord(["C#4", "E4"])
    n2i.duration.quarterLength = 1.5
    mi_izquierda.append(n2i)    #2.25
    
    silencio1 = note.Rest()
    silencio1.quarterLength = .75
    mi_izquierda.append(silencio1)  #3
    
    n3i = note.Note("G#3")
    n3i.duration.quarterLength = 0.75
    mi_izquierda.append(n3i)    #3.75
    
    n4i = chord.Chord(["B3", "D#4"])
    n4i.duration.quarterLength = 1.5
    mi_izquierda.append(n4i)    #5.25
    
    silencio2 = note.Rest()
    silencio2.quarterLength = .75
    mi_izquierda.append(silencio2)  #6
    
    n5i = note.Note("F#3")
    n5i.duration.quarterLength = 0.75
    mi_izquierda.append(n5i)    #6.75
    
    n6i = chord.Chord(["A#3", "C#4"])
    n6i.duration.quarterLength = 1.25
    mi_izquierda.append(n6i)    #8
    
    n7i = chord.Chord(["A#3", "C#4"])
    n7i.duration.quarterLength = .75
    mi_izquierda.append(n7i)    #8.75
    
    n8i = chord.Chord(["G#3", "C#4"])
    n8i.duration.quarterLength = 1.25
    mi_izquierda.append(n8i)    #10
    
    silencio2 = note.Rest()
    silencio2.quarterLength = 1.5
    mi_izquierda.append(silencio2)  #11.5


def primera_melodia_derecha(mi_derecha):
    silencio = note.Rest()
    silencio.quarterLength = .75
    derecha.append(silencio)
    
    n1d = chord.Chord(["G#4", "E5"])
    n1d.duration.quarterLength = 0.375
    mi_derecha.append(n1d)

    n2d = note.Note("D#5")
    n2d.duration.quarterLength = 0.375
    mi_derecha.append(n2d)  #1.5

    n3d = note.Note("B4")
    n3d.quarterLength = .75
    mi_derecha.append(n3d)  #2.25

    n4d = note.Note("G#4")
    n4d.quarterLength = .75
    mi_derecha.append(n4d)  #3

    n5d = note.Note("B4")
    n5d.duration.quarterLength = 1.5
    #n5d.tie = tie.Tie("start")
    mi_derecha.append(n5d)  #4.5
    
    n5d2 = note.Note("F#4")
    n5d2.duration.quarterLength = .75
    #n5d2.tie = tie.Tie("stop")
    #mi_derecha.append(n5d2)

    n6d = note.Note("G#4")
    n6d.quarterLength = .75
    mi_derecha.append(n6d)  #5.25

    n7d = note.Note("B4")
    n7d.duration.quarterLength = .75
    mi_derecha.append(n7d)  #6

    n8d = note.Note("A#4")
    n8d.duration.quarterLength = 2
    mi_derecha.append(n8d)  #8

    n9d = note.Note("F#4")
    n9d.quarterLength = .75
    mi_derecha.append(n9d)  #8.75

    n10d = note.Note("D#4")
    n10d.duration.quarterLength = 1.25
    mi_derecha.append(n10d) #10

    n11d = note.Note("D#4")
    n11d.duration.quarterLength = .75
    mi_derecha.append(n11d) #10.75

    n12d = note.Note("F#4")
    n12d.quarterLength = .75
    mi_derecha.append(n12d) #11.5
    
    
def segunda_melodia_izquierda(mi_izquierda):
    n1i = note.Note("A3") # La
    n1i.duration.quarterLength = .75
    mi_izquierda.append(n1i) #.75
    
    n2i = chord.Chord(["C#4", "E4"])
    n2i.duration.quarterLength = 1.5
    mi_izquierda.append(n2i)    #2.25
    
    silencio1 = note.Rest()
    silencio1.quarterLength = .75
    mi_izquierda.append(silencio1)  #3
    
    n3i = note.Note("G#3")
    n3i.duration.quarterLength = 0.75
    mi_izquierda.append(n3i)    #3.75
    
    n4i = chord.Chord(["B3", "D#4"])
    n4i.duration.quarterLength = 1.5
    mi_izquierda.append(n4i)    #5.25
    
    silencio2 = note.Rest()
    silencio2.quarterLength = .75
    mi_izquierda.append(silencio2)  #6
    
    n5i = note.Note("F#3")
    n5i.duration.quarterLength = 0.75
    mi_izquierda.append(n5i)    #6.75
    
    n6i = chord.Chord(["A#3", "C#4"])
    n6i.duration.quarterLength = 1.25
    mi_izquierda.append(n6i)    #8
    
    n7i = chord.Chord(["A#3", "C#4"])
    n7i.duration.quarterLength = .75
    mi_izquierda.append(n7i)    #8.75
    
    n8i = chord.Chord(["G#3", "C#4"])
    n8i.duration.quarterLength = .75
    mi_izquierda.append(n8i)    #9.5
    
    n9i = note.Note("F#3")
    n9i.duration.quarterLength = .75
    mi_izquierda.append(n9i)    #10.25
    
    n10i = note.Note("A#3")
    n10i.duration.quarterLength = .75
    mi_izquierda.append(n10i)    #11
    
    n11i = note.Note("C#4")
    n11i.duration.quarterLength = .75
    mi_izquierda.append(n11i)    #11.75 TOTAL = 23.25
    
    
def segunda_melodia_derecha(mi_derecha):
    silencio = note.Rest()
    silencio.quarterLength = .75
    derecha.append(silencio)
    
    n1d = chord.Chord(["G#4", "E5"])
    n1d.duration.quarterLength = 0.375
    mi_derecha.append(n1d)

    n2d = note.Note("D#5")
    n2d.duration.quarterLength = 0.375
    mi_derecha.append(n2d)  #1.5

    n3d = note.Note("B4")
    n3d.quarterLength = .75
    mi_derecha.append(n3d)  #2.25

    n4d = note.Note("G#4")
    n4d.quarterLength = .75
    mi_derecha.append(n4d)  #3

    n5d = note.Note("B4")
    n5d.duration.quarterLength = 1.5
    #n5d.tie = tie.Tie("start")
    mi_derecha.append(n5d)  #4.5
    
    n5d2 = note.Note("F#4")
    n5d2.duration.quarterLength = .75
    #n5d2.tie = tie.Tie("stop")
    #mi_derecha.append(n5d2)

    n6d = note.Note("G#4")
    n6d.quarterLength = .75
    mi_derecha.append(n6d)  #5.25

    n7d = note.Note("B4")
    n7d.duration.quarterLength = .75
    mi_derecha.append(n7d)  #6

    n8d = note.Note("A#4")
    n8d.duration.quarterLength = 2
    mi_derecha.append(n8d)  #8

    n9d = chord.Chord(["F#4", "A#4"])
    n9d.quarterLength = .75
    mi_derecha.append(n9d)  #8.75

    n10d = note.Note("F#5")
    n10d.duration.quarterLength = 1.25
    mi_derecha.append(n10d) #10 TOTAL = 21.5


primera_melodia_izquierda(izquierda)
segunda_melodia_izquierda(izquierda)
primera_melodia_derecha(derecha)
segunda_melodia_derecha(derecha)

pentagrama.append([izquierda, derecha])
#pentagrama.show('text')
#pentagrama.show()

#izquierda.show()
#derecha.show()
pentagrama.show("midi")

#pentagrama.write('midi', 'by_your_side.midi')