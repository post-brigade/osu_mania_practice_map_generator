from src.classes import LongNote, Note, TimingPoint

from .column_and_bpm_helpers import column_to_x, random_column


# not currently used
def randomize_notes(notes: list[Note | LongNote], key_count) -> list[Note | LongNote]:
    notes_no_chords: list[Note | LongNote] = []

    for i in range(len(notes)):
        current_note = notes[i]
        if i < len(notes) - 1 and current_note.time == notes[i + 1].time:
            continue

        notes_no_chords.append(current_note)

    random_notes: list[Note | LongNote] = []

    for i in range(len(notes_no_chords)):
        banned_columns: set[int] = set()
        current_note = notes_no_chords[i]
        banned_columns.add(notes_no_chords[i - 1].column)

        if i > 0:
            banned_columns.add(notes_no_chords[i - 1].column)

        current_note.column = random_column(banned_columns, key_count)
        current_note.x = column_to_x(current_note.column, key_count)
        random_notes.append(current_note)

    return random_notes
