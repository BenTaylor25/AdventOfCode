
FILENAME = "dial_turns.txt"

def read_dial_turns_from_file(filename):
    with open(filename) as f:
        dial_turns = [x.strip('\n') for x in f.readlines()]
    return dial_turns

def turn_dial(dial_value, dial_turn, min=0, max=99):
    assert min <= dial_value <= max, dial_value
    range = max - min + 1

    turn_count = int(dial_turn[1:])

    if dial_turn[0] == 'L':
        turn_count *= -1

    dial_value += turn_count

    while dial_value < min:
        dial_value += range
    while dial_value > max:
        dial_value -= range

    return dial_value

def get_password_from_dial_instructions(filename):
    dial_turns = read_dial_turns_from_file(filename)

    dial_value = 50
    password = 0

    for dial_turn in dial_turns:
        dial_value = turn_dial(dial_value, dial_turn)

        if dial_value == 0:
            password += 1

    return password


if __name__ == "__main__":
    password = get_password_from_dial_instructions(FILENAME)
    print(password)