const fs = require('fs');


function readCommands(filename) {
    try {
        let data = fs.readFileSync(filename, 'utf8');
        return data.split('\n');
    } catch (e) {
        console.error(e);
        return []
    }
}

function getCurrentObjLocation(base, chain) {
    let current = base;

    chain.forEach(key => {
        current = current[key];
    });

    return current;
}

function makeObj(lines) {
    let base = {'/': {}};
    let chain = [];

    let listingDirs = false;

    lines.forEach(line => {
        let lineArr = line.split(' ');
        let isCommand = lineArr[0] == '$';

        if (isCommand) { 
            listingDirs = false; 
        } else if (listingDirs) {
            let current = getCurrentObjLocation(base, chain);
            if (lineArr[0] == 'dir') {
                current[lineArr[1]] = {};
            } else {
                current[lineArr[1]] = lineArr[0]
            }
        }

        if (isCommand && lineArr[1] == 'cd') {
            if (lineArr[2] == '..') {
                chain.pop();
            } else {
                chain.push(lineArr[2]);
            }
        }

        else if (isCommand && lineArr[1] == 'ls') {
            listingDirs = true;
        }
        
    });


    return base;
}

function readDirsAsArr(filename) {
    let lines = readCommands(filename);
    let obj = makeObj(lines);

    console.log(obj['/']);

    return; //
}

function main() {
    let dirs = readDirsAsArr('dirSample.txt');
}
main();
