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


#/mnt/c/Users/postb/Desktop/to_convert
def main():
    key_count = 7
    should_print = True
    map_path = "/mnt/c/Users/postb/Desktop/to_convert/to_convert.osu"
    new_map_path = "/mnt/c/Users/postb/Desktop/to_convert/converted.osu"

    normal_lines, timing_points, notes = read_map(map_path, key_count) # tested
    print(notes)
    sorted_notes = sorted(notes, key = lambda note: (note.time, note.column))

    note_instructions = notes_to_note_instructions(sorted_notes) # tested

    timing_changes_from_map = get_timing_changes(timing_points) # tested

    final_timing_changes = note_instructions_to_timing_changes(timing_changes_from_map, note_instructions)  # tested

    generated_notes = generate_notes_with_timing_points(final_timing_changes, notes[-1], key_count) # tested

    notes_with_chords = add_chords(generated_notes, key_count) # tested

    generate_note_matrix(notes_with_chords, final_timing_changes, should_print, key_count) # tested

    new_map = build_new_map(normal_lines, final_timing_changes, notes_with_chords) #tested

    write_map(new_map, new_map_path) # tested

    print()
    for x in range(1, 8):
        print(column_to_x(x, 7))

if __name__ == "__main__":
    main()
