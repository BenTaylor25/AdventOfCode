from sum_of_valid_expressions import *

OPERATORS.append("||")
OPERATOR_LAMBDAS.append(lambda a, b : int(str(a) + str(b)))

if __name__ == "__main__":
    print(sum_of_valid_expressions(FILENAME, OPERATORS))
