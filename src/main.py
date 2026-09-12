import sys

from src.functions import (
    add_chords,
    build_new_map,
    generate_note_matrix,
    generate_notes_with_timing_points,
    get_cli_arguments,
    get_timing_changes,
    get_user_input,
    note_instructions_to_timing_changes,
    notes_to_note_instructions,
    read_map,
    write_map,
)


def main():
    should_print = True

    if len(sys.argv) == 1:
        map_path, new_map_path, key_count, generation_type = get_user_input()

    else:
        map_path, new_map_path, key_count, generation_type = get_cli_arguments(sys.argv)

    normal_lines, timing_points, notes = read_map(map_path, key_count) # tested

    sorted_notes = sorted(notes, key = lambda note: (note.time, note.column))

    note_instructions = notes_to_note_instructions(sorted_notes) # tested

    timing_changes_from_map = get_timing_changes(timing_points) # tested

    final_timing_changes = note_instructions_to_timing_changes(timing_changes_from_map, note_instructions)  # tested

    notes_to_map = generate_notes_with_timing_points(final_timing_changes, notes[-1], key_count) # tested

    notes_to_map = add_chords(notes_to_map, generation_type, key_count) # tested

    generate_note_matrix(notes_to_map, final_timing_changes, should_print, key_count) # tested

    new_map = build_new_map(normal_lines, final_timing_changes, notes_to_map) #tested

    write_map(new_map, new_map_path) # tested

if __name__ == "__main__":
    main()
