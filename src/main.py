from src.functions import (
    add_chords,
    build_new_map,
    column_to_x,
    generate_note_matrix,
    generate_notes_with_timing_points,
    get_timing_changes,
    note_instructions_to_timing_changes,
    notes_to_note_instructions,
    read_map,
    write_map,
)


def main():
    key_count = 7
    map_path = "./testing/maps/read/hazy_test_notes_to_note_instructions.osu"
    new_map_path = "./testing/maps/write/hazy_test_notes_to_note_instructions.osu"

    normal_lines, timing_points, notes = read_map(map_path, key_count) # tested

    sorted_notes = sorted(notes, key = lambda note: (note.time, note.column))

    note_instructions = notes_to_note_instructions(sorted_notes) # tested

    timing_changes_from_map = get_timing_changes(timing_points) # tested

    timing_changes_with_instructions = note_instructions_to_timing_changes(timing_changes_from_map, note_instructions)  # tested

    generated_notes = generate_notes_with_timing_points(timing_changes_with_instructions, notes[-1], key_count) # tested

    notes_with_chords = add_chords(generated_notes, key_count)

    generate_note_matrix(notes_with_chords, timing_changes_with_instructions, key_count)

    new_map = build_new_map(normal_lines, timing_changes_with_instructions, notes_with_chords)
    write_map(new_map, new_map_path)

    for x in range(1, 8):
        print(column_to_x(x, 7))

if __name__ == "__main__":
    main()
