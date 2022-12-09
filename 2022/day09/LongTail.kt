import java.io.BufferedReader
import java.io.File
import java.io.FileReader
import java.io.IOException

fun abs(x: Int): Int {
    if (x < 0) {
        return -x;
    }
    return x;
}

class Pos (
    var x: Int = 0,
    var y: Int = 0
) {}

class PositionSimLongTail (
    var ropePos: Array<Pos> = arrayOf(Pos(), Pos(), Pos(), Pos(), Pos(), Pos(), Pos(), Pos(), Pos(), Pos()),
    var tailTipVisited: Array<Pos> = arrayOf(Pos())
) {

    fun move(h: Int, v: Int) {
        var oldPos = Pos()
        oldPos.x = ropePos[0].x
        oldPos.y = ropePos[0].y

        ropePos[0].x += h
        ropePos[0].y += v

        var n = 1
        var shouldMoveMore = true
        while (n < 10 && shouldMoveMore) {
            // get distance between n and n-1
            val xdist = abs(ropePos[n].x - ropePos[n-1].x) 
            val ydist = abs(ropePos[n].y - ropePos[n-1].y) 
            // println("" + xdist + " " + ydist)

            if (xdist <= 1 && ydist <= 1) {
                shouldMoveMore = false
            } else {

                if (ropePos[n].y == ropePos[n-1].y) {
                    if (ropePos[n].x < ropePos[n-1].x) {
                        ropePos[n].x += 1
                    } else {
                        ropePos[n].x -= 1
                    }
                }
                else if (ropePos[n].x == ropePos[n-1].x) {
                    if (ropePos[n].y < ropePos[n-1].y) {
                        ropePos[n].y += 1
                    } else {
                        ropePos[n].y -= 1
                    }
                }
                else {
                    if (ropePos[n].x < ropePos[n-1].x) {
                        ropePos[n].x += 1
                    } else {
                        ropePos[n].x -= 1
                    }

                    if (ropePos[n].y < ropePos[n-1].y) {
                        ropePos[n].y += 1
                    } else {
                        ropePos[n].y -= 1
                    }
                }

                if (n == 9 && !tailTipVisited.contains(ropePos[n])) {
                    tailTipVisited += ropePos[n]
                }

                n += 1
            }
        }
        // println()
    }

    fun moveNorth(times: Int) {
        for (i in 1..times) {
            move(0, 1)
        }
    }

    fun moveSouth(times: Int) {
        for (i in 1..times) {
            move(0, -1)
        }
    }

    fun moveEast(times: Int) {
        for (i in 1..times) {
            move(1, 0)
        }
    }

    fun moveWest(times: Int) {
        for (i in 1..times) {
            move(-1, 0)
        }
    }

    fun getSetSize(): Int {
        return tailTipVisited.count()
    }
}

fun readFile(filename: String): Array<String> {
    val file = File(filename)
    var arr: Array<String> = arrayOf()

    try {
        BufferedReader(FileReader(file)).use { br ->
            var line: String?
            while (br.readLine().also { line = it } != null) {
                arr += line.toString()
            }
        }
    } catch (e: IOException) {
        e.printStackTrace()
    }

    return arr
}

fun main() {
    var ps = PositionSimLongTail()

    val fileArr = readFile("./ropeMoveSample2.txt")
    for (line in fileArr) {
        // println("LINE: " + line)
        var linesplit = line.split(" ")

        when (linesplit[0]) {
            "U" -> {
                ps.moveNorth(Integer.parseInt(linesplit[1]))
            }
            "D" -> {
                ps.moveSouth(Integer.parseInt(linesplit[1]))
            }
            "L" -> {
                ps.moveWest(Integer.parseInt(linesplit[1]))
            }
            "R" -> {
                ps.moveEast(Integer.parseInt(linesplit[1]))
            }
        }
    }

    println(ps.getSetSize())
}

