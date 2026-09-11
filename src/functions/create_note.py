from src.classes import Note


def create_note(note_list: list[str], key_count: int) -> Note:
    column = int(note_list[0])
    y = int(note_list[1])
    time = float(note_list[2])
    type= int(note_list[3])
    hit_sound = int(note_list[4])
    hit_sample = str(note_list[5])

    new_note = Note(
        column,
        y,
        time,
        type,
        hit_sound,
        hit_sample,
        key_count
    )
    return new_note
