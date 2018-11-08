# Final Fantasy Tactics - Command Line Edition

Final Fantasy Tactics is a JRPG in which battles take place on chessboard-like stages and characters are moved around like chess pieces.
I thought it'd be fun to recreate the mechanics of this game in several languages (this one being Python) as an exercise to force me to
use as many aspects of the Python language as possible.  

At this point most of the mechanics have been set up, and battles can take place in a way similar to CTB battle system in the original
FFT game. Sometime in the future, I'll work on making navigating the map more user-friendly (as user-friendly as you can make the CLI anyway).  

At the end of every battle reset the attack and defense stats on units  
All other stats will persist

or add augments dict to units. detecs value, ailments, etc


I need a way to track a unit's current position on a stage
current_pos
function update_pos

how to measure distance of tiles? Distance would be the distance in the tile id's number and letter in alphabet
do units belong to a given tile?

## Next

- units take turns


- allow only valid movements on a stage
- change repr functions to be Python expressions
- add str data model methods
- units have a way that they are facing!!!

## Database

- connect code to database
- load items and abilities
- upload game.db to git
- upload maps.db to git

# Game Flow

- Turn on game
- start new game
  - load items
  - load jobs
  - load abilities
  - create new party
  - create main character name and bday
