FILENAME = "worksheet.txt"

def get_worksheet_as_2d_arr_from_file(use_sample):
    filename = "sample_" * use_sample + FILENAME

    with open(filename) as f:
        lines = [x.strip('\n') for x in f.readlines()]

    arr = [line.split(' ') for line in lines]
    arr = [list(filter(lambda x : x != '', inner)) for inner in arr]
    print(arr)
    return arr

def convert_worksheet(worksheet):
    for row in range(len(worksheet) - 1):
        for col in range(len(worksheet[row])):
            worksheet[row][col] = int(worksheet[row][col])

def one_or_zero_start(operator):
    if operator == '+':
        return 0
    elif operator == '*':
        return 1
    assert False, operator

def calculate_worksheet_answers(worksheet):
    operators = [operator for operator in worksheet[-1]]
    answers = [one_or_zero_start(operator) for operator in operators]

    for row in worksheet[:-1]:
        for i in range(len(answers)):
            if operators[i] == '+':
                answers[i] += row[i]
            elif operators[i] == '*':
                answers[i] *= row[i]
            else:
                assert False, f"{i} : {operators}"

    return answers

if __name__ == "__main__":
    worksheet = get_worksheet_as_2d_arr_from_file(False)
    convert_worksheet(worksheet)
    answers = calculate_worksheet_answers(worksheet)
    print(sum(answers))
