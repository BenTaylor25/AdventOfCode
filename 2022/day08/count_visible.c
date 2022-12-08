#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

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

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf("%d ", trees[i*SIZE + j]);
        }
        printf("\n");
    }

    free(trees);
}
