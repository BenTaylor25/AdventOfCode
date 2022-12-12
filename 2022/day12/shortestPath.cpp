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

int * get_start(vector<vector<int>>* elevations) {
    static int start[] = {-1, -1};

    for (int y = 0; y < (*elevations).size(); y++) {
        for (int x = 0; x < (*elevations)[y].size(); x++) {
            if ((*elevations)[y][x] == (int)'S' - (int)'a') {
                (*elevations)[y][x] = 0;
                start[0] = y;
                start[1] = x;
            }
        }
    }

    return start;
}

int * get_end(vector<vector<int>>* elevations) {
    static int end[] = {-1, -1};

    for (int y = 0; y < (*elevations).size(); y++) {
        for (int x = 0; x < (*elevations)[y].size(); x++) {
            if ((*elevations)[y][x] == (int)'E' - (int)'a') {
                (*elevations)[y][x] = 25;
                end[0] = y;
                end[1] = x;
            }
        }
    }

    return end;
}

int main() {
    auto elevations = read_elevations("./elevationSample.txt");
    int *start = get_start(&elevations);
    int *end = get_end(&elevations);

    std::cout << "y: " << start[0] << ", x: " << start[1] << std::endl;
    std::cout << "y: " << end[0] << ", x: " << end[1] << std::endl << std::endl;

    for (vector<int> x : elevations) {
        for (int y : x) {
            std::cout << y << "  ";
        }
        std::endl(std::cout);
    }
}
