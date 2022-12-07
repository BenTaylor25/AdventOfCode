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
                current[lineArr[1]] = --lineArr[0]
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

function objToArr(obj) {
    if (typeof obj == 'object') {
        let arr = [];
        for (const [_, v] of Object.entries(obj)) {
            arr.push(objToArr(v));
        }
        return arr;
    }
    return obj;
}

function readDirsAsArr(filename) {
    let lines = readCommands(filename);
    let obj = makeObj(lines);
    let arr = objToArr(obj)[0];

    // console.log(obj['/']);
    // console.log();
    // console.log(arr);

    return arr;
}

function recSum(arr) {
    sum = 0;

    arr.forEach(num => {
        if (typeof num == 'object') {   // Array
            sum += recSum(num);
        } else {
            sum += num;
        }
    });

    return sum;
}

function getAllSums(dirsArr) {
    let allSums = [];
    allSums.push(recSum(dirsArr))

    dirsArr.forEach(item => {
        if (typeof item == 'object') {   // Array
            let recSums = getAllSums(item);
            allSums.push(...recSums);
        }
    });

    return allSums;
}

function main() {
    let dirsArr = readDirsAsArr('dirSample.txt');
    let allSums = getAllSums(dirsArr);
    let filteredSums = allSums.filter(x => { return x <= 100000 });
    let filteredSumsSum = recSum(filteredSums);

    // console.log(allSums);
    // console.log(filteredSums);
    console.log(filteredSumsSum);
}
main();
