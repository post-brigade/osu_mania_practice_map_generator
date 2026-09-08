For now only hard-coded to read/write files manually set in main().

Works off a timed map and reads notes on the map as instructions by column.

Note generation starts out off.

Default generation is 16th notes at maps bpm. (1/4 snap)

Tracks uninherited timing points, but unsure how it will handle lots of tempo changes.

Notes in column:

  1: start generation
  
  2: stop generation
  
  3: double bpm
  
  4: halve bpm
  
Currently only generates dense 7 key chordstream; need to start with 7 key map.

Generates sample of patterning in console.

Patterning is currently based on 4/4 meter; odd meters will have accents in weird spots.

Doesn't update metadata yet.
