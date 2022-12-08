#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define SIZE 5

void read_ints(const char* file_name, int ** arr)
{
    FILE* file = fopen (file_name, "r");
    int f_i = 0;

    // int arr[SIZE][SIZE];
    int a_r = 0;
    int a_c = 0;

    while (!feof (file)) {
        fscanf (file, "%1d ", &f_i);
        // printf ("%1d ", f_i);

        if (f_i == '\n') {
            a_r++;
            a_c = 0;
        } else {
            arr[a_r][a_c] = f_i;
            a_c++;
        }
    }
    fclose (file);
}


int main() {
    int * trees = malloc(SIZE * SIZE * sizeof(int));
    read_ints("./treesSample.txt", &trees);

    // display trees
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf("%d ", trees[i*SIZE + j]);
        }
        printf("\n");
    }

    int visible = 0;

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            bool on_perim = i == 0 || j == 0 || i == SIZE-1 || j == SIZE-1;

            if (on_perim) {
                visible++;
            } else {
                bool left_hidden = false;
                for (int k = 0; k < j; k++) {
                    left_hidden = left_hidden || trees[i*SIZE + k] >= trees[i*SIZE + j];
                }

                bool right_hidden = false;
                for (int k = j+1; k < SIZE; k++) {
                    right_hidden = right_hidden || trees[i*SIZE + k] >= trees[i*SIZE + j];
                }

                bool up_hidden = false;
                for (int k = 0; k < i; k++) {
                    up_hidden = up_hidden || trees[k*SIZE + j] >= trees[i*SIZE + j];
                }

                bool down_hidden = false;
                for (int k = i+1; k < SIZE; k++) {
                    down_hidden = down_hidden || trees[k*SIZE + j] >= trees[i*SIZE + j];
                }

                // printf("%d %d %d %d\n", left_hidden, right_hidden, up_hidden, down_hidden);

                if (!(left_hidden && right_hidden && up_hidden && down_hidden)) {
                    visible++;
                }
            }
        }
    }

    printf("%d\n", visible);

    free(trees);
}
