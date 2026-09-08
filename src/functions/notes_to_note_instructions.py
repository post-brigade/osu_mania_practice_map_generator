from src.classes import Note


def notes_to_note_instructions(notes: list[Note]) -> list[tuple[int, float]]:
    instructions: list[tuple[int, float]] = []
    start = False

    for note in notes:
        if note.column == 1 or note.column == 2:
            if note.column == 1 and start == False:
                instructions.append((note.column,note.time))
                start = True

            if note.column == 2 and start == True:
                instructions.append((note.column,note.time))
                start = False

        if note.column == 3 or note.column == 4:
            instructions.append((note.column,note.time))

    return instructions
