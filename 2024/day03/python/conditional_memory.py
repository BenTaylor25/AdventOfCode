from multiplication_memory import *

DO = "do()"
DONT = "don't()"

def remove_between(string, remove_delim, include_delim):
    including = True

    new_string = ""

    for idx in range(0, len(string)):
        if string.startswith(remove_delim, idx):
            including = False
        if string.startswith(include_delim, idx):
            including = True

        if including:
            new_string += string[idx]

    return new_string

def conditional_memory(filename):
    memory_str = get_memory_str_from_file(filename)
    memory_str = remove_between(memory_str, DONT, DO)

    indices_to_check = get_potential_starting_indices(memory_str, MUL_FIRST_TOKEN)
    operands_of_valid_expressions = get_operands_of_valid_expressions(memory_str, indices_to_check)

    return sum([x * y for (x, y) in operands_of_valid_expressions])

if __name__ == "__main__":
    print(conditional_memory(FILENAME))
