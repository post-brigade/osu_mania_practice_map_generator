from src.classes import LongNote


def create_long_note(note_list: list[str], key_count: int) -> LongNote:
    column = int(note_list[0])
    y = int(note_list[1])
    time = float(note_list[2])
    note_type = int(note_list[3])
    hit_sound = int(note_list[4])
    end_time = float(note_list[5])
    hit_sample = note_list[6]

    new_note = LongNote(
        column,
        y,
        time,
        note_type,
        hit_sound,
        end_time,
        hit_sample,
        key_count

    )
    return new_note
