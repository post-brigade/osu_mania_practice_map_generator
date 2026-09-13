

def get_difficulty_name(generation_type, key_count) -> str:
    if not generation_type or not (1 <= generation_type <= 5):
        raise ValueError("Invalid generation type")

    if key_count == 4:
       difficulties = [
           "[4k Stream]",
           "[4k Light Jumpstream]",
           "[4k Dense Jumpstream]",
           "[4k Light Handstream]",
           "[4k Dense Handstream]",
       ]

    elif key_count == 7:
        difficulties = [
            "[7k Stream]",
            "[7k Light Chordstream]",
            "[7k Light-ish Chordstream]",
            "[7k Dense-ish Chordstream]",
            "[7k Dense Chordstream]",
        ]
    else:
        raise ValueError("Invalid key count")

    return difficulties[generation_type - 1]
