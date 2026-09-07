from src.classes import Note


def notes_to_note_instructions(notes: list[Note]) -> list[tuple[int, float]]:
    instructions = []
    for note in notes:
        if 1 <= note.column <= 4:
            instructions.append((note.column,note.time))

    return instructions
