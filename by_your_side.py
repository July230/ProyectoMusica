from music21 import note, stream, chord

pentagrama = stream.Score()
derecha = stream.Part()
izquierda = stream.Part()

n1i = note.Note("A3") # La
n1i.duration.quarterLength = .75
izquierda.append(n1i)

silencio = note.Rest()
silencio.quarterLength = .75
derecha.append(silencio)

n1d = chord.Chord(["G#4", "E5"])
n1d.duration.quarterLength = 0.375
derecha.append(n1d)

n2d = note.Note("D#5")
n2d.duration.quarterLength = 0.375
derecha.append(n2d)

n3d = note.Note("B4")
n3d.quarterLength = .75
derecha.append(n3d)

n4d = note.Note("G#4")
n4d.quarterLength = .75
derecha.append(n4d)

n5d = note.Note("B4")
n5d.duration.quarterLength = 1.5
derecha.append(n5d)

n6d = note.Note("G#4")
n6d.quarterLength = .75
derecha.append(n6d)

n7d = note.Note("B4")
n7d.duration.quarterLength = .75
derecha.append(n7d)

n8d = note.Note("A#4")
n8d.duration.quarterLength = 2
derecha.append(n8d)

n9d = note.Note("F#4")
n9d.quarterLength = .75
derecha.append(n9d)

n10d = note.Note("D#4")
n10d.duration.quarterLength = 2.25
derecha.append(n10d)

n11d = note.Note("D#4")
n11d.duration.quarterLength = .75
derecha.append(n11d)

n12d = note.Note("F#4")
n12d.quarterLength = .75
derecha.append(n12d)

pentagrama.append([izquierda, derecha])
pentagrama.show()
#pentagrama.show("midi")