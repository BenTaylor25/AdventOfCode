
Today was hard!

7.5-hours-hard, but I did it... kind of.

I spent over an hour battling with the Kotlin compiler to get the first part working, but eventually did it with no help.

This is my first time using Kotlin, and the second part got too much.  
Part of that was due to the fact that I didn't completely understand how movement was meant to work; for example consider:
```
. H . .               H 1 . .
. . 1 .   move left   . . 2 .
. . . 2     ->        . a b c
. . 3 .               . . . .

should 3
go to a: copy the diagonal movement of 2,
go to c: take 2's previous position,
go to b: get closer to 2
```  
After struggling for over 3 hours, I consulted the internet for inspiration.  
I found [this](https://topaz.github.io/paste/#XQAAAQBXCQAAAAAAAAARiEJHiiMzw3cPM/1Vl+2nx/DqKkM2yi+HVdpp+qLiqZwdO8DftYzG7xETHPvhjXpLhVBtGHxiJr7yn4tjI2iyRb/7n/gXbNlVB4eTFC9qDqbwwm0sASx0Z8gruN/cpWo3PsqaJQNRlzQ47B8QLNgr2bUJjl8BZcN0NVVirhGXWQi4bttrV6pezOOAK/ZdraXGryuUsNApUzbrGEJCSEUZkxzt1dCmsSXHs3aMqiBUX5GwRQ3QMMYIBPAcCDea0C9WjAUreNLk+ondYhGF8Cxb2hwJcWlLUuP1rHy1b6anwj7rb0VU+iPKaZtZm19xlZujEL3HkOJlyFWwJFJyF6AG6SuFJvoqEhVcrqYed2BPKv0ccDlD2fe7Udakb1nUvWDZ45j0Xk8e4YLpwdhjSUJU7v9BVYhPHUeJC2/8ecOywDr2/2fFpNVatPQ2e2Q7v/ZLeOTpEy2LweGSSa8RgLNFChmWag3u2lObV1DpCVUgfrj7S4rBc053CghV222Y+h/muiYlqZpArexEooJpH2QfP53rBLK9Ai3t+wplMZsAyEcRoIuxvDzqz0tqHSB4RX6xSaG2OJoZLJyRX2v66EwERXStSn3yzG0+c1MUHnDbCCIa6rHfKgY5NNtUQoQJ2eF388wPTIsJVXxGna3P2GuHEveAb46Yl6Es80I+dZ1uovGIjj3vjMRSwjmiZwDCb/QO44imXEq+ZfC9TJTIqyYpQGYAqH55VQ760zTCBTAp63sucfbv1GrHzD84WIrscDIuks+k6o76PCG4XkgXKnVsmVViRG8ubvJALgNvFInw5xAPJ9wON2nt00CIVOOe/aEOopO+SNGH4cUi1b1FS9kCbdqKPB7rbBaOqGqkHWY9TOr1GJwIocX2THOLG+6eW3VRDbYuBLYBLFKv4oYRWAfAqQvIV6uUQtD2mS7plOCjlC1QQN8hfYpX1VcC/rH05V5c5sqNhfmaSzj0xs4esFi37/E8i1joSP/4RloC); a very elegant solution, but one that I didn't feel comfortable translating to Kotlin due to the complex numbers. 

My plan was to convert the Python into a simpler form (using arrays instead of complex numbers), and then translate my Python into Kotlin.  
I spent over an hour debugging a pass-by-reference issue and eventually decided that my Python version was enough.  

I was aiming for 15 different languages for the first 15 days of Advent of Code, and I've half met that today. One of the reasons I wanted to do the 15 languages was to gain exposure to more different syntaxes and ways of thinking, and I think I've achieved that.
