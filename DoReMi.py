from music21 import note

# Crear los archivos midi do re y mi
note.Note("C").write('midi', "Notas/do.mid")
note.Note("D").write('midi', "Notas/re.mid")
note.Note("E").write('midi', "Notas/mi.mid")