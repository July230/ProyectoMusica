from music21 import note

# Nota
# A - La
# B - Si
# C - Do
# D - Re
# E - Mi
# F - Fa
# G - Sol
miNota = note.Note("C")

# Abrir el editor de partituras con la nota
miNota.show()

# Abrir el reproductor de midi's con un archivo midi con la nota Do
miNota.show('midi')

print(miNota)
print(miNota.name)
print(miNota.octave)
print(miNota.pitch)
print(miNota.pitch.frequency)
print(miNota.pitch.spanish)