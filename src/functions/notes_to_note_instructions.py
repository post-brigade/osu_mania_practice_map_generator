from src.classes import Note

instruction_list = list[tuple[int, float]]

def notes_to_note_instructions(notes: list[Note]) -> tuple[instruction_list, instruction_list]:
    start_stop_instructions = []
    bpm_instructions = []
    start = False

    for note in notes:
        if note.column == 1 or note.column == 2:
            if note.column == 1 and start == False:
                start_stop_instructions.append((note.column,note.time))
                start = True

            if note.column == 2 and start == True:
                start_stop_instructions.append((note.column,note.time))
                start = False

        if note.column == 3 or note.column == 4:
            bpm_instructions.append((note.column,note.time))

    return start_stop_instructions, bpm_instructions
