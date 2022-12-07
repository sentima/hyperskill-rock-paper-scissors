# hyperskill-rock-paper-scissors
rock-paper-scissors little game\
##### This program:

* Asks your name and greats you;
* Reads rating.txt and checks whether it contains an entry with the current username. If yes, ut uses the score specified in the file as a starting point. If not, starts the score from 0;
* Reads the input with the list of options for the game (options are separated by comma). If the input is an empty line, it plays with the default options (whis is usual rock-paper-scissor);
* Plays the game by the rules defined in the previous stages and reads the user's input;
* If the input is `!exit`, outputs `Bye!` and stops the game;
* if the input is `!rating`, it prints the user score
* If the input is the name of the option, then game picks a random variant for itself and output a line with the result of the game:
  * Loss: `Sorry, but the computer chose <option>`
  * Draw: `There is a draw (<option>)`
  * Win: `Well done. The computer chose <option> and failed`
* For each draw, adds 50 points to the score. For each user's win, adds 100 to their score. In case of a loss, dones't change the score;
* If input corresponds to anything else, outputs `Invalid input`;
* Restarts the game (with the same options defined before the start of the game).

this project is a part of the educational process in JetBrains Academy course **"Python Core"**
