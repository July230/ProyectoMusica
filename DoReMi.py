from music21 import note

# Crear los archivos midi do re y mi
note.Note("C").write('midi', "Notas/do.mid")
note.Note("D").write('midi', "Notas/re.mid")
note.Note("E").write('midi', "Notas/mi.mid")
note.Note("F").write('midi', "Notas/fa.mid")
note.Note("G").write('midi', "Notas/sol.mid")
note.Note("A").write('midi', "Notas/la.mid")
note.Note("B").write('midi', "Notas/si.mid")
note.Note("C5").write('midi', "Notas/do5.mid")