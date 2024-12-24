FILENAME = "multiplication_memory.txt"
SAMPLE_FILENAME = "sample_multiplication_memory.txt"

MUL_FIRST_TOKEN = "mul("
MUL_SECOND_TOKEN = ","
MUL_FINAL_TOKEN = ")"

def get_memory_str_from_file(filename):
    with open(filename) as f:
        str = f.readline()

    return str

def get_potential_starting_indices(memory_str, token):
    return [i for i in range(len(memory_str)) if memory_str.startswith(token, i)]

def scan_for(str, sub_str, starting_idx):
    for i in range(len(sub_str)):
        full_str_idx = starting_idx + i

        if str[full_str_idx] != sub_str[i]:
            return False
    return True

def collect_chars_between(str, end_char, starting_idx):
    chars_between = ""

    idx = starting_idx
    while idx < len(str) and str[idx] != end_char:
        chars_between += str[idx]
        idx += 1

    return idx < len(str), chars_between

def get_operands_of_valid_expressions(memory_str, indices_to_check):
    operands_of_valid_expressions = []

    for idx in indices_to_check:
        if not scan_for(memory_str, MUL_FIRST_TOKEN, idx):
            continue

        idx += len(MUL_FIRST_TOKEN)

        valid, first_operand_str = collect_chars_between(memory_str, MUL_SECOND_TOKEN, idx)
        if not valid or not first_operand_str.isdigit():
            continue
        first_operand = int(first_operand_str)

        idx += len(first_operand_str) + 1

        valid, second_operand_str = collect_chars_between(memory_str, MUL_FINAL_TOKEN, idx)
        if not valid or not second_operand_str.isdigit():
            continue
        second_operand = int(second_operand_str)

        operands_of_valid_expressions.append((first_operand, second_operand))

    return operands_of_valid_expressions


def multiplication_memory(filename):
    memory_str = get_memory_str_from_file(filename)

    indices_to_check = get_potential_starting_indices(memory_str, MUL_FIRST_TOKEN)
    operands_of_valid_expressions = get_operands_of_valid_expressions(memory_str, indices_to_check)

    return sum([x * y for (x, y) in operands_of_valid_expressions])

if __name__ == "__main__":
    print(multiplication_memory(FILENAME))
