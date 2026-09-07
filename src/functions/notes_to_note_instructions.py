from src.classes import Note

instruction_list = list[tuple[int, float]]

def notes_to_note_instructions(notes: list[Note]) -> tuple[instruction_list, instruction_list]:
    start_stop_instructions = []
    bpm_instructions = []
    for note in notes:
        if 1<= note.column <= 2:
            start_stop_instructions.append((note.column,note.time))

        if 3<= note.column <= 4:
            bpm_instructions.append((note.column,note.time))

    return start_stop_instructions, bpm_instructions
