from guard_postitions import *

def pack_location_direction(location, direction):
    return f"{location}, {direction}"

def detect_loop(temp_map, guard_location, guard_direction):
    previous_location_directions = set()
    guard_on_map = True

    while guard_on_map:
        # Check if the guard has already been at this location with this
        # direction. (If so, a loop has been created).
        if pack_location_direction(guard_location, guard_direction) in previous_location_directions:
            return True

        previous_location_directions.add(pack_location_direction(guard_location, guard_direction))

        # Calculate forward location.
        forward_location = [location + direction for location, direction in zip(guard_location, guard_direction)]
        forward_location_on_map = \
            0 <= forward_location[0] < len(temp_map) and \
            0 <= forward_location[1] < len(temp_map[0])

        # Check if guard is on the map.
        if not forward_location_on_map:
            return False

        # Should turn if there is an obstruction in the forward location.
        should_turn = temp_map[forward_location[0]][forward_location[1]] == OBSTRUCTION_CHAR

        if should_turn:
            # Turn.
            idx = DIRECTIONS.index(guard_direction)
            new_idx = (idx + 1) % len(DIRECTIONS)
            new_direction = DIRECTIONS[new_idx]
            guard_direction = new_direction

        else:
            # Step.
            guard_location = forward_location

def guard_loop(filename):
    """
    This is very much a brute force solution but it works...
    It does, however, take about 4 minutes to run :)
    I want to do a better solution.
    """
    map_ = get_map_from_file(filename)

    loops_from_one_more_obstacle = 0

    # Place a new obstruction in every location where one is allowed.
    # Then run the temporary map through a simulation that detects
    # if a loop has been created.
    for i in range(len(map_)):
        print(f"Calculating row {i+1} of {len(map_)}")
        for j in range(len(map_[i])):
            if map_[i][j] not in (GUARD_CHAR, OBSTRUCTION_CHAR):
                temp_map = [row[:] for row in map_]
                temp_map[i][j] = OBSTRUCTION_CHAR

                guard_location = get_guard_starting_point(map_)
                guard_direction = UP_DIR

                loop_is_created = detect_loop(temp_map, guard_location, guard_direction)
                if loop_is_created:
                    loops_from_one_more_obstacle += 1

    return loops_from_one_more_obstacle

if __name__ == "__main__":
    print(guard_loop(FILENAME))
