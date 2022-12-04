use std::fs;

fn read_pair() -> Vec<[i32; 4]> {
    // run from count_contains dir
    let contents = fs::read_to_string("./assignmentSample.txt")
        .expect("Cannot read file.");

    let lines = contents.split('\n');

    let mut pairs_as_vec: Vec<[i32;4]> = vec![];

    for line in lines {
        if line != "" {
            let assignments = line.split(',');

            let mut pair: [i32; 4] = [0; 4];
            let mut i: usize = 0;
            for assignment in assignments {
                let times = assignment.split('-');

                for time in times {
                    // println!("{}", time);
                    let num = match time.parse::<i32>() {
                        Ok(int) => int,
                        Err(e) => { panic!("{}", e) }
                    };
                    pair[i] = num;
                    i += 1;
                }
            }
            pairs_as_vec.push(pair);
        }
    }

    // for p in pairs_as_vec {
    //     println!("{} {} {} {}", p[0], p[1], p[2], p[3]);
    // }
    return pairs_as_vec
}

fn main() {
    read_pair();
}
