Run from root of project: 

$python3 -m src.main \<path to input map\> \<path to output\> \<key count\> \<density setting\> 

Key count: 4 or 7

Density setting: 1 to 5: 1 is single stream, 5 is dense handstream for 4key, dense chordstream for 7k

Works off a timed map and reads notes on the map as instructions by column.

Note generation starts out off.

Default generation is 16th notes at maps bpm. (1/4 snap)

Tracks uninherited timing points, but unsure how it will handle lots of tempo changes.

Notes in column:

  1: start generation
  
  2: stop generation
  
  3: double bpm
  
  4: halve bpm
  
Works with 4key and 7key.

Generates sample of map in console.

Patterning is currently based on 4/4 meter; odd meters will have accents in weird spots.

Doesn't update metadata yet.
