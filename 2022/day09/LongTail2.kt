import java.io.BufferedReader
import java.io.File
import java.io.FileReader
import java.io.IOException

class Pos (
    var x: Int = 0,
    var y: Int = 0
) {}

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

fun abs(x: Int): Int {
    if (x < 0) {
        return -x
    }
    return x
}

fun main() {
    var chain: Array<Pos> = arrayOf(Pos(), Pos(), Pos(), Pos(), Pos(), Pos(), Pos(), Pos(), Pos(), Pos())
    var visited: Array<Pos> = arrayOf(Pos())

    val fileArr = readFile("./ropeMoveSample2.txt")

    for (move in fileArr) {
        val movesplit = move.split(" ")

        for (i in 1..Integer.parseInt(movesplit[1])) {
            if (movesplit[0] == "U") {
                chain[0].y += 1
            }
            else if (movesplit[0] == "D") {
                chain[0].y -= 1
            }
            else if (movesplit[0] == "L") {
                chain[0].x -= 1
            }
            else if (movesplit[0] == "R") {
                chain[0].x += 1
            }

            for (k in 1..9) {   // 9 inclusive
                val xsquared = (chain[k].x - chain[k-1].x) * (chain[k].x - chain[k-1].x)
                val ysquared = (chain[k].y - chain[k-1].y) * (chain[k].y - chain[k-1].y)

                if (xsquared + ysquared < 4) {
                    break
                }

                if (chain[k].y == chain[k-1].y) {
                    if (chain[k].x < chain[k-1].x) {
                        chain[k].x += 1
                    } else {
                        chain[k].x -= 1
                    }
                }

                else if (chain[k].x == chain[k-1].x) {
                    if (chain[k].y < chain[k-1].y) {
                        chain[k].y += 1
                    } else {
                        chain[k].y -= 1
                    }
                }

                else {
                    if (chain[k].x < chain[k-1].x) {
                        chain[k].x += 1
                    } else {
                        chain[k].x -= 1
                    }

                    if (chain[k].y < chain[k-1].y) {
                        chain[k].y += 1
                    } else {
                        chain[k].y -= 1
                    }
                }

            }
        }

        if (true) { // scope
            val p = Pos()
            p.x = chain[9].x
            p.y = chain[9].y

            var contains = false
            for (v in visited) {
                if (p.x == v.x && p.y == v.y) {
                    contains = true
                }
            }

            if (!contains) {
                visited += p
            }
        }
    }

    println(visited.count())
}
