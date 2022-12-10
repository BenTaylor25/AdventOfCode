
def readfile(filename)
    arr = []
    File.foreach(filename).with_index do |line, line_num|
        arr.append(line.split(" "))
    end
    return arr
end


def main
    filelines = readfile "signalSample2.txt"

    important_cycles = [20, 60, 100, 140, 180, 220]
    important_signal_strengths = []

    cycle = 1
    fileind = 0
    x = 1
    searching = false
    cycle_to_stop_search = -1
    sum_to_add_after_search = 0

    # puts "x: #{x}  cycle: #{cycle}"
    while fileind < filelines.length()

        for i in 0..important_cycles.length()-1
            if cycle == important_cycles[i]
                # puts
                # puts "start of cycle #{cycle}"
                # puts "x: #{x}"

                signal_strength = cycle * x
                puts "signal strength: #{signal_strength}"
                important_signal_strengths.append(signal_strength)
            end
        end

        if !searching
            if filelines[fileind][0] == "noop"
                searching = true
                cycle_to_stop_search = cycle + 1
                sum_to_add_after_search = 0
            elsif filelines[fileind][0] == "addx"
                searching = true
                cycle_to_stop_search = cycle + 2
                sum_to_add_after_search = filelines[fileind][1].to_i
            end
        end

        cycle += 1

        if searching
            if cycle == cycle_to_stop_search
                searching = false
                x += sum_to_add_after_search
                fileind += 1
            end
        end
    end
    puts

    puts "sum of signal strengths: #{important_signal_strengths.sum}"
end
main
