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
    var headPos: Pos,
    var tailPos: Pos,
    var tailVisited: Array<Pos> = arrayOf(Pos())
) {

    fun move(h: Int, v: Int) {
        var oldheadPos = headPos

        headPos.x += h
        headPos.y += v //

        if (tailShouldMove()) {
            tailx = oldheadx
            taily = oldheady

            if (!tailVisited.contains(tailx*10000 + taily)) {
                tailVisited = tailVisited.plus(tailx*10000 + taily)
            }
        }
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

    fun tailShouldMove(): Boolean {
        return abs(tailx - headx) > 1 || abs(taily - heady) > 1
    }

    fun getSetSize(): Int {
        return tailVisited.count()
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
    var ps = PositionSim()

    val fileArr = readFile("./ropeMoveActual.txt")
    for (line in fileArr) {
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

