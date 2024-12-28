import itertools

FILENAME = "equation_operands.txt"
SAMPLE_FILENAME = "sample_equation_operands.txt"

VALUE_DELIMETER = ':'
OPERAND_DELIMETER = ' '

OPERATORS = ["+", "*"]
OPERATOR_LAMBDAS = [
    lambda a, b : a + b,
    lambda a, b : a * b
]

def get_value_and_operands_from_file(filename):
    values = []
    operand_lists = []

    with open(filename) as f:
        for line in f.readlines():
            line = line.strip('\n')

            value, operands = line.split(VALUE_DELIMETER)

            value = int(value.strip())
            values.append(value)

            operands = operands.strip().split(OPERAND_DELIMETER)
            operands = [int(operand.strip()) for operand in operands]
            operand_lists.append(operands)

    return values, operand_lists

def compute_expression_left_to_right(operand_list, operators):
    # Create a copy to prevent in-place modification.
    operand_list = operand_list[:]

    operator_expr_idx = 0

    while len(operand_list) > 1:
        a = operand_list.pop(0)
        b = operand_list.pop(0)

        operator_const_idx = OPERATORS.index(operators[operator_expr_idx])
        operator_lambda = OPERATOR_LAMBDAS[operator_const_idx]
        operator_expr_idx += 1

        c = operator_lambda(a, b)
        operand_list.insert(0, c)

    return operand_list[0]

def check_operand_list(value, operand_list, valid_operators):
    operator_permutations = list(itertools.product(valid_operators, repeat=len(operand_list) - 1))

    for operator_permutation in operator_permutations:
        if value == \
            compute_expression_left_to_right(operand_list, operator_permutation):
            return True
    return False

def sum_of_valid_expressions(filename, operators):
    values, operand_lists = get_value_and_operands_from_file(filename)

    values_of_valid_expressions = []

    for value, operand_list in zip(values, operand_lists):
        expression_has_valid_solution = \
            check_operand_list(value, operand_list, operators)

        if expression_has_valid_solution:
            values_of_valid_expressions.append(value)

    return sum(values_of_valid_expressions)


if __name__ == "__main__":
    print(sum_of_valid_expressions(FILENAME, OPERATORS))
