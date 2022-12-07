const fs = require('fs');


function readDirs(filename) {
    try {
        let data = fs.readFileSync(filename, 'utf8');
        return data.split('\n');
    } catch (e) {
        console.error(e);
        return []
    }
}


function main() {
    let lines = readDirs('dirSample.txt');

    if (lines) {
        console.log(lines);
    }
}
main();
