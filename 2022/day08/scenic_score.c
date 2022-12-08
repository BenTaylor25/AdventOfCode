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
    // for (int i = 0; i < SIZE; i++) {
    //     for (int j = 0; j < SIZE; j++) {
    //         printf("%d ", trees[i*SIZE + j]);
    //     }
    //     printf("\n");
    // }

    int max_scenic_score = 0;

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            int k;

            int left_score = 0;
            k = j-1;
            while (k >= 0) {
                left_score++;
                if (trees[i*SIZE + k] >= trees[i*SIZE + j]) {
                    break;
                }
                k--;
            }

            int right_score = 0;
            k = j+1;
            while (k < SIZE) {
                right_score++;
                if (trees[i*SIZE + k] >= trees[i*SIZE + j]) {
                    break;
                }
                k++;
            }

            int up_score = 0;
            k = i-1;
            while (k >= 0) {
                up_score++;
                if (trees[k*SIZE + j] >= trees[i*SIZE + j]) {
                    break;
                }
                k--;
            }

            int down_score = 0;
            k = i+1;
            while (k < SIZE) {
                down_score++;
                if (trees[k*SIZE + j] >= trees[i*SIZE + j]) {
                    break;
                }
                k++;
            }

            // printf("%d %d %d %d\n", left_score, right_score, up_score, down_score);
            int scenic_score = left_score * right_score * up_score * down_score;
            if (scenic_score > max_scenic_score) {
                max_scenic_score = scenic_score;
            }
        }
    }

    printf("%d\n", max_scenic_score);

    free(trees);
}

