from password_dials import *

def turn_dial(dial_value, dial_turn, min=0, max=99):
    assert min <= dial_value <= max, dial_value
    range = max - min + 1

    turn_count = int(dial_turn[1:])

    if dial_turn[0] == 'L':
        turn_count *= -1

    old_dial_value = dial_value
    dial_value += turn_count

    dial_tick_over = 0

    first_iteration = True
    while dial_value < min:
        dial_value += range
        if not (first_iteration and old_dial_value == 0):
            dial_tick_over += 1
        first_iteration = False

    while dial_value > max:
        dial_value -= range
        if dial_value != 0:
            dial_tick_over += 1

    # if dial_tick_over != 0:
    #     print(dial_turn, f"{old_dial_value} -> {dial_value}", dial_tick_over)

    return dial_value, dial_tick_over

def get_password_from_dial_instructions_any_tick_over(filename):
    dial_turns = read_dial_turns_from_file(filename)

    dial_value = 50
    password = 0

    for dial_turn in dial_turns:
        dial_value, dial_tick_over = turn_dial(dial_value, dial_turn)

        password += dial_tick_over

        if dial_value == 0:
            password += 1

    return password


if __name__ == "__main__":
    password = get_password_from_dial_instructions_any_tick_over(FILENAME)
    print(password)
