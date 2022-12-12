#include <iostream>
#include <vector>
#include <fstream>
#include <climits>

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

    int *up = new int[2];
    int *down = new int[2];
    int *left = new int[2];
    int *right = new int[2];

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

int dijkstras_alg(vector<vector<int>>* elevations, int *start, int *end) {
    int dist[(*elevations).size()][(*elevations)[0].size()];
    int prev[(*elevations).size()][(*elevations)[0].size()][2];
    bool visited[(*elevations).size()][(*elevations)[0].size()];
    double unvisited_dist[(*elevations).size()][(*elevations)[0].size()];
    for (int r = 0; r < (*elevations).size(); r++) {
        for (int c = 0; c < (*elevations)[0].size(); c++) {
            visited[r][c] = false;
            unvisited_dist[r][c] = INT_MAX;
            prev[r][c][0] = -1;
            prev[r][c][1] = -1;
        }
    }
    unvisited_dist[start[0]][start[1]] = 0;

    while (!visited[end[0]][end[1]]) {
        int x[]{0, 0};
        while (visited[x[0]][x[1]]) {
            x[1]++;
            if (x[1] > (*elevations)[0].size()) {
                x[1] = 0;
                x[0]++;
            }
        }

        for (int r = 0; r < (*elevations).size(); r++) {
            for (int c = 0; c < (*elevations)[0].size(); c++) {
                if (!visited[r][c]) {
                    if (unvisited_dist[r][c] < unvisited_dist[x[0]][x[1]]) {
                        x[0] = r;
                        x[1] = c;
                    }
                }
            }
        }

        visited[x[0]][x[1]] = true;

        if (!(x[0] == end[0] && x[1] == end[1])) {
            auto neighbours = get_neigbours(elevations, x);

            for (int *n : neighbours) {
                if (!visited[n[0]][n[1]]) {
                    double dist_of_arc = 1;   // adjacent
                    double current_dist = unvisited_dist[x[0]][x[1]] + dist_of_arc;
                    if (current_dist < unvisited_dist[n[0]][n[1]]) {
                        unvisited_dist[n[0]][n[1]] = current_dist;
                        prev[n[0]][n[1]][0] = x[0];
                        prev[n[0]][n[1]][1] = x[1];
                    }
                }
            }
            for (int *i : neighbours) {
                delete i;
            }
        }
    }
    return dist[end[0]][end[1]];
}

int main() {
    auto elevations = read_elevations("./elevationSample.txt");
    int *start = get_start(&elevations);
    int *end = get_end(&elevations);

    int shortest = dijkstras_alg(&elevations, start, end);

    std::cout << shortest << std::endl;

    // std::cout << "y: " << start[0] << ", x: " << start[1] << std::endl;
    // std::cout << "y: " << end[0] << ", x: " << end[1] << std::endl << std::endl;

    // for (vector<int> x : elevations) {
    //     for (int y : x) {
    //         std::cout << y << "  ";
    //     }
    //     std::endl(std::cout);
    // }
}
