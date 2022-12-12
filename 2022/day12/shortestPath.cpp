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

bool is_valid_neighbour(vector<vector<int>>* elevations, int* from, int* to) {
    // assume from is in grid
    if (to[0] < 0 || to[0] > elevations->size() || to[1] < 0 || to[1] > elevations[0].size()) {
        return false;   // out of grid
    }
    return (*elevations)[from[0]][from[1]] + 1 <= (*elevations)[to[0]][to[1]];
}

vector<int*> get_neigbours(vector<vector<int>>* elevations, int* from) {
    vector<int*> neighbours;

    int *up, *down, *left, *right;

    up[0] = from[0]-1;
    up[1] = from[1];
    if (is_valid_neighbour(elevations, from, up)) {
        neighbours.push_back(up);
    }

    down[0] = from[0]+1;
    down[1] = from[1];
    if (is_valid_neighbour(elevations, from, down)) {
        neighbours.push_back(down);
    }

    left[0] = from[0];
    left[1] = from[1]-1;
    if (is_valid_neighbour(elevations, from, left)) {
        neighbours.push_back(left);
    }

    right[0] = from[0];
    right[1] = from[1]+1;
    if (is_valid_neighbour(elevations, from, right)) {
        neighbours.push_back(right);
    }

    return neighbours;
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
