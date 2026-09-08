import copy

from src.classes import LongNote, Note

from .column_and_bpm_helpers import column_to_x, random_column


def create_chord_note(note: Note | LongNote, banned_columns: set[int], key_count = 7) -> Note | LongNote:
    new_note = copy.copy(note)
    new_note.column = random_column(banned_columns, key_count)
    new_note.x = column_to_x(new_note.column, key_count)

    return new_note
