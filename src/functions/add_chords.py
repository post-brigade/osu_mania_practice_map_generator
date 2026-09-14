import copy
import math

from src.classes import LongNote, Note

from .column_and_bpm_helpers import column_to_x, random_column


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
    new_banned_columns = banned_columns
    next_banned_columns: set[int] = set()
    for i in range(size_of_chord):
        chord_note = create_chord_note(note, new_banned_columns, key_count)
        new_banned_columns.add(chord_note.column)
        next_banned_columns.add(chord_note.column)
        chord.append(chord_note)
    sorted_chord = sorted(chord, key = lambda note: note.column)
    return sorted_chord, next_banned_columns


def create_chord_note(note: Note | LongNote, banned_columns: set[int], key_count = 7) -> Note | LongNote:
    new_note = copy.copy(note)
    new_note.column = random_column(banned_columns, key_count)
    new_note.x = column_to_x(new_note.column, key_count)

    return new_note


def seven_key_chords(notes: list[Note], generation_type: int) -> list[Note]:
    key_count = 7
    notes_with_chords:list[Note | LongNote] = []
    banned_columns: set[int] = set()
    chord_index = 0


    for i in range(len(notes)):
        chord_index, banned_columns = check_for_breaks(notes, i, banned_columns, chord_index)

        if chord_index % 16 == 0:
            if generation_type in (2, 4):
                chord_size = 3
            elif generation_type == 3:
                chord_size = 4
            elif generation_type == 5:
                chord_size = 5
            else:
                raise ValueError("Invalid generation value")

            chord, banned_columns = add_chord(notes[i], banned_columns, chord_size, key_count)
            notes_with_chords.extend(chord)
            chord_index += 1
            continue

        if chord_index % 8 == 0 and generation_type == 5:
            chord_size = 4
            chord, banned_columns = add_chord(notes[i], banned_columns, chord_size, key_count)
            notes_with_chords.extend(chord)
            chord_index += 1
            continue

        elif chord_index % 4 == 0:
            if generation_type in (3, 5):
                chord_size = 3
            elif generation_type in (2, 4):
                chord_size = 2
            else:
                raise ValueError("Invalid generation value")

            chord, banned_columns = add_chord(notes[i], banned_columns, chord_size, key_count)
            notes_with_chords.extend(chord)
            chord_index += 1
            continue

        elif chord_index % 2 == 0 and generation_type in (4, 5):
            chord_size = 2
            chord, banned_columns = add_chord(notes[i], banned_columns, chord_size, key_count)
            notes_with_chords.extend(chord)
            chord_index += 1
            continue

        else:
            new_note = copy.copy(notes[i])
            new_note.column = random_column(banned_columns, key_count)
            new_note.x = column_to_x(new_note.column, key_count)
            banned_columns = {new_note.column}
            notes_with_chords.append(new_note)
            chord_index += 1

    return notes_with_chords


def four_key_chords(notes: list[Note], generation_type: int) -> list[Note]:
    key_count = 4
    notes_with_chords:list[Note | LongNote] = []
    banned_columns: set[int] = set()
    chord_index = 0

    for i in range(len(notes)):
        chord_index, banned_columns = check_for_breaks(notes, i, banned_columns, chord_index)

        if chord_index % 4 == 0:
            if generation_type in (4, 5):
                chord_size = 3
            elif generation_type in (2, 3):
                chord_size = 2
            else:
                raise ValueError("Invalid generation value")

            chord, banned_columns = add_chord(notes[i], banned_columns, chord_size, key_count)
            notes_with_chords.extend(chord)
            chord_index += 1
            continue

        elif chord_index % 2 == 0 and generation_type in (3, 5):
            chord_size = 2
            chord, banned_columns = add_chord(notes[i], banned_columns, chord_size, key_count)
            notes_with_chords.extend(chord)
            chord_index += 1
            continue

        else:
            new_note = copy.copy(notes[i])
            new_note.column = random_column(banned_columns, key_count)
            new_note.x = column_to_x(new_note.column, key_count)
            banned_columns = {new_note.column}
            notes_with_chords.append(new_note)
            chord_index += 1

    return notes_with_chords


def check_time_index(notes_with_chords, banned_columns, note_index, time_index):
    if len(notes_with_chords) < abs(note_index):
        return banned_columns

    if notes_with_chords[note_index].time_index == time_index - 1:
        banned_columns.add(notes_with_chords[note_index].column)
        check_time_index(notes_with_chords, banned_columns, note_index - 1, time_index)

    return banned_columns


def check_for_breaks(notes: list[Note], i: int, banned_columns: set[int], chord_index: int) -> tuple[int, set[int]]:
    new_banned_columns = banned_columns
    if 1 < i:
        time_step = notes[i].time - notes[i - 1].time
        previous_step = notes[i - 1].time - notes[i - 2].time

        if time_step > previous_step * 4 or math.isclose(previous_step, time_step * 4, abs_tol=.1):
            new_banned_columns = set()
            chord_index = 0

    return chord_index, new_banned_columns
