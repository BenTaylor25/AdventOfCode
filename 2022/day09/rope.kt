fun abs(x: Int): Int {
    if (x < 0) {
        return -x;
    }
    return x;
}

class PositionSim (
    var headx: Int = 0,
    var heady: Int = 0,
    var tailx: Int = 0,
    var taily: Int = 0,
    var tailVisited: Array<Int> = arrayOf()
) {

    fun move(h: Int, v: Int) {
        var oldheadx = headx
        var oldheady = heady

        headx += h
        heady += v

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

fun main() {
    var ps = PositionSim()

    ps.moveNorth(2)

    println(ps.getSetSize())
}
