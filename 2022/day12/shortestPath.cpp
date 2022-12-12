#include <iostream>
#include <vector>
#include <fstream>

using std::vector;
using std::string;

vector<vector<int>> read_elevations(string filename) {
    vector<vector<int>> elevations;

    std::fstream file;
    file.open(filename, std::ios::in);
    if (file.is_open()) {
        string line;
        while (getline(file, line)) {
            vector<int> chrs;
            for (char x : line) {
                chrs.push_back((int)x - (int)'a');
            }
            elevations.push_back(chrs);
        }

        file.close();
    }

    return elevations;
}

int main() {
    auto elevations = read_elevations("./elevationSample.txt");

    for (vector<int> x : elevations) {
        for (int y : x) {
            std::cout << y << "  ";
        }
        std::endl(std::cout);
    }
}
