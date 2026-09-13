from src.classes import LongNote, Note, TimingPoint

from .column_and_bpm_helpers import column_to_x, x_to_column


def generate_note_matrix(notes: list[Note | LongNote], timing_changes: list[TimingPoint], should_print:bool, key_count: int):
    if not notes:
        return

    GRAY = rgb_to_console_color(100,100,100)
    RESET = "\033[0m"

    time_index = 0
    is_barline = time_index % 8 == 0
    note_matrix = [create_row(is_barline, key_count, GRAY, RESET)]
    note = " ▆▆▆ "

    # for long notes
    # note_length = " ███ "
    # note_tail = "▃▃▃"

    barline_note = f"{GRAY}▁{RESET}▆▆▆{GRAY}▁{RESET}"

    for i in range(len(notes)):
        if time_index >= 32:
            break
        current_note = notes[i]
        current_column = x_to_column(current_note.x, key_count)
        note_matrix[time_index][current_column - 1] = barline_note if is_barline else note

        if i < len(notes) - 1 and current_note.time != notes[i + 1].time:
            time_index += 1
            is_barline = time_index % 8 == 0
            note_matrix.append(create_row(is_barline, key_count, GRAY, RESET))

    if should_print:
        for i in range (len(note_matrix) - 1, -1, -1):
            print("".join(note_matrix[i]))
            print()

    # for testing
    return note_matrix


def rgb_to_console_color(r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m"


def create_row(is_barline: bool, key_count: int, barline_color, default_color) -> list[str]:
    column = f"{barline_color}▁▁▁▁▁{default_color}" if is_barline else "     "
    row = [column for _ in range(key_count)]
    return row
