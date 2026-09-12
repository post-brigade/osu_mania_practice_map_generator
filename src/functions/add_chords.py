from src.classes import LongNote, Note

from .column_and_bpm_helpers import random_column
from .create_chord_note import create_chord_note


def add_chords(notes: list[Note | LongNote], generation_type: int, key_count) -> list[Note | LongNote]:
    if generation_type == 1:
        return notes

    if key_count == 7:
        notes_with_chords = seven_key_chords(notes, generation_type)
    elif key_count == 4:
        notes_with_chords = four_key_chords(notes, generation_type)
    else:
        raise ValueError("Invalid key count")

    return notes_with_chords


def add_chord(note: Note, banned_columns: set[int], size_of_chord: int,  key_count: int) -> tuple[list[Note], set[int]]:
    chord:list[Note | LongNote] = []
    for i in range(size_of_chord - 1):
        note = create_chord_note(note, banned_columns, key_count)
        note.column = random_column(banned_columns, key_count)
        banned_columns.add(note.column)
        chord.append(note)

    return chord, banned_columns


def seven_key_chords(notes, generation_type):
    key_count = 7
    notes_with_chords:list[Note | LongNote] = []
    banned_columns: set[int] = set()

    for i in range(len(notes)):
        notes_with_chords.append(notes[i])
        banned_columns = {notes[i].column}

        if i > 0:
            banned_columns.add(notes[i - 1].column)

        if i < len(notes) - 1:
            banned_columns.add(notes[i + 1].column)

        if generation_type == 5 and i % 8 == 0:
            chord_size = 4
            chord, banned_columns = add_chord(notes[i], banned_columns, chord_size, key_count)
            sorted_chord = sorted(chord, key = lambda note: note.column)
            notes_with_chords.extend(sorted_chord)
            continue

        if i % 4 == 0:
            if generation_type in (2, 4):
                chord_size = 2
            elif generation_type == 3:
                chord_size = 4
            elif generation_type == 5:
                chord_size = 3
            else:
                continue

            chord, banned_columns = add_chord(notes[i], banned_columns, chord_size, key_count)
            sorted_chord = sorted(chord, key = lambda note: note.column)
            notes_with_chords.extend(sorted_chord)
            continue

        if generation_type in (4, 5) and i % 2 == 0:
            chord_size = 2
            chord, banned_columns = add_chord(notes[i], banned_columns, chord_size, key_count)
            sorted_chord = sorted(chord, key = lambda note: note.column)
            notes_with_chords.extend(sorted_chord)
            continue

    return notes_with_chords


def four_key_chords(notes: list[Note], generation_type: int):
    key_count = 4
    notes_with_chords:list[Note | LongNote] = []
    banned_columns: set[int] = set()

    for i in range(len(notes)):
        notes_with_chords.append(notes[i])
        banned_columns = {notes[i].column}

        if i < len(notes) - 1:
            notes[i + 1].column = random_column(banned_columns, key_count)
            banned_columns.add(notes[i + 1].column)

        if i > 0:
            banned_columns.add(notes[i - 1].column)

        if (generation_type == 4 or generation_type == 5) and i % 4 == 0:
            if 0 < i < len(notes) - 1:
                notes[i + 1].column = notes[i - 1].column
            banned_columns = {notes[i].column, notes[i - 1].column}
            chord_size = 3
            chord, banned_columns = add_chord(notes[i], banned_columns, chord_size, key_count)
            sorted_chord = sorted(chord, key = lambda note: note.column)
            notes_with_chords.extend(sorted_chord)
            continue

        if (generation_type == 2 or generation_type == 3) and i % 4 == 0:
            chord_size = 2
            chord, banned_columns = add_chord(notes[i], banned_columns, chord_size, key_count)
            sorted_chord = sorted(chord, key = lambda note: note.column)
            notes_with_chords.extend(sorted_chord)
            continue

        if (generation_type == 3 or generation_type == 5) and i % 2 == 0:
            chord_size = 2
            chord, banned_columns = add_chord(notes[i], banned_columns, chord_size, key_count)
            sorted_chord = sorted(chord, key = lambda note: note.column)
            notes_with_chords.extend(sorted_chord)
            continue

    return notes_with_chords
