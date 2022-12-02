import 'dart:io';

// col 1: elf picks
// A: rock, B: paper, C: scissors

// col 2: player needs to
// X: lose, Y: draw, Z: win

/**
 * returns [elfRps, playerRps]
 * 
 * 0 = rock,
 * 1 = paper,
 * 2 = scissors
 */
List<int> getGameDecision(List lineAsList) {
  assert('ABC'.contains(lineAsList[0]));
  assert('XYZ'.contains(lineAsList[1]));

  int elfAscii = lineAsList[0].codeUnitAt(0);
  int playerAscii = lineAsList[1].codeUnitAt(0);

  return [elfAscii - 65, playerAscii - 88];
}

/**
 * return [bool playerWins, bool playerLoses]
 */
List<bool> winLose(List game) {
  assert([0, 1, 2].contains(game[0]));
  assert([0, 1, 2].contains(game[1]));

  bool playerLoses = false;
  if (game[0] - 1 == game[1] || game[0] + 2 == game[1]) {
    playerLoses = true;
  }

  bool playerWins = false;
  if (game[0] + 1 == game[1] || game[0] - 2 == game[1]) {
    playerWins = true;
  }

  return [playerWins, playerLoses];
}

/**
 * given elfMove and goal (to lose/draw/win)
 *  
 * 0: rock, 1: paper, 2: scisors
 */
int getChoice(List<int> decisions) {
  // elf rock/paper/scisors
  int eRps = decisions[0];
  // loss/draw/win
  int ldw = decisions[1] - 1; // l: -1, d: 0, w: 1

  // player rock/paper/scissors
  int pRps = eRps + ldw; // range: -1 - 3
  pRps %= 3;

  return pRps;
}

void main() {
  File('./rpsSample.txt').readAsString().then((String contents) {
    int score = 0;

    contents.split('\n').forEach((line) {
      if (line != '') {
        List<int> decisions = getGameDecision(line.split(' '));

        // lose, draw or win
        score += 3 * decisions[1];

        // rock: +1, paper: +2, scissors: +3
        score += 1 + getChoice(decisions);
      }
    });

    print(score);
  });
}
