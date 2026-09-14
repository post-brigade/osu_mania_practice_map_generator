

Run from root of project: 

$python3 -m src.main \<path to input map\> \<key count\> \<density setting\> 

Or run with main.sh:

Follow the prompts, will accept windows and linux paths (if using WSL).

Key count: 4 or 7.

Density setting: 

  7k: 1: Stream 2: Light Chordstream 3: Light-ish Chordstream 4: Dense-ish Chordstream 5: Dense Chordstream

  4k: 1: Stream 2: Light Jumpstream 3: Dense Jumpstream 4: Light Handstream 5: Dense Handstream 

The map to generate from should be timed, with no notes except intended instructions.

Note generation starts out off.

A note in:

  Column 1: Starts note generation at 1/4 snap.

  Column 2: Stops note generation.

  Column 3: Doubles generation bpm.

  Column 3: Halves generation bpm.

Final note in map ends generation. Can be any column.

A sample of the map will be generated in the console.

Patterning is based on 4/4 meter.

The generated map is saved in the same folder as the input map, with the density setting tacked on the front of the file name.

Long note support someday. Maybe.
