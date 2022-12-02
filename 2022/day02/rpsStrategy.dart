// import 'dart:async';
import 'dart:io';

/**
 * returns [elfRps, playerRps]
 * 
 * 0 = rock,
 * 1 = paper,
 * 2 = scissors
 */
List getGameDecision(List lineAsList) {
  assert('ABC'.contains(lineAsList[0]));
  assert('XYZ'.contains(lineAsList[1]));

  int elfAscii = lineAsList[0].codeUnitAt(0);
  int playerAscii = lineAsList[1].codeUnitAt(0);

  return [elfAscii - 65, playerAscii - 88];
}

/**
 * return [bool playerWins, bool playerLoses]
 */
List winLose(List game) {
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
    contents.split('\n').forEach((line) {
      if (line != '') {
        List decision = getGameDecision(line.split(' '));
        print(winLose(decision));
        print(decision);
      }
    });
  });
}
