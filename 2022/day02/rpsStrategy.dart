// import 'dart:async';
import 'dart:io';

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

void main() {
  File('./rpsSample.txt').readAsString().then((String contents) {
    int score = 0;

    contents.split('\n').forEach((line) {
      if (line != '') {
        List<int> decisions = getGameDecision(line.split(' '));
        // print(winLose(decision));
        // print(decision);

        List<bool> results = winLose(decisions);
        if (results[0]) {
          // player wins
          score += 6;
        } else if (results[0] == results[1]) {
          // draw
          score += 3;
        }

        // rock: +1, paper: +2, scissors: +3
        score += 1 + decisions[1];
      }
    });

    print(score);
  });
}
