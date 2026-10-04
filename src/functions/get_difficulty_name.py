import math


def get_difficulty_name(generation_type, key_count, density_rating) -> str:
    if not math.isclose(density_rating, 0, abs_tol=0.01):
        difficulty = f"[7k Bursty Custom density {density_rating}]"
        print(difficulty)
        return difficulty

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
            "[7k Bursty Stream]",
            "[7k Bursty Light Chordstream]",
            "[7k Bursty Light-ish Chordstream]",
            "[7k Bursty Dense-ish Chordstream]",
            "[7k Bursty Dense Chordstream]",
        ]
    else:
        raise ValueError("Invalid key count")

    return difficulties[generation_type - 1]
