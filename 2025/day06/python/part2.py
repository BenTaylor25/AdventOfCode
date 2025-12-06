from part1 import *

def transpose_worksheet(worksheet):
    operators = worksheet[-1]
    worksheet_values = worksheet[:-1]

    t_cols = len(worksheet_values)
    t_rows = len(worksheet_values[0])

    transposed_values = [[0 for _ in range(t_cols)] for _ in range(t_rows)]
    for i in range(t_cols):
        for j in range(t_rows):
            transposed_values[j][i] = worksheet_values[i][j]

    transposed = transposed_values
    transposed.append(operators)

    return transposed

def convert_problem_to_values(problem):

    # Oh no.
    # Spaces matter now :o
    # I need to re-read the file differently.
    # However it is too late and I have work
    # tomorrow so I must resign for now :(

    pass
    # return problem_values

def convert_to_values(worksheet):
    for i in range(len(worksheet) - 1):
        worksheet[i] = convert_problem_to_values(worksheet[i])

def convert_worksheet_2(worksheet):
    worksheet = transpose_worksheet(worksheet)
    print(worksheet)
    convert_to_values(worksheet)
    return worksheet

if __name__ == '__main__':
    worksheet = get_worksheet_as_2d_arr_from_file(True)
    worksheet = convert_worksheet_2(worksheet)
    answers = calculate_worksheet_answers(worksheet)
    print(sum(answers))
