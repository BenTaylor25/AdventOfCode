
FILENAME = "disk_map.txt"
SAMPLE_FILENAME = "sample_disk_map.txt"

EMPTY_SPACE = '.'

def get_disk_map_from_file(filename):
    with open(filename) as f:
        line = f.readline()

    return line

def expand_disk_map(disk_map):
    disk_expanded = []

    char_is_file = True
    file_id = 0

    for char in disk_map:
        # Disk Map indicates the size of the next section.
        size = int(char)

        # The next section will consist of blocks of either a file id or
        # empty space.
        next_n_blocks = file_id if char_is_file else EMPTY_SPACE

        # Insert blocks.
        for _ in range(size):
            disk_expanded.append(next_n_blocks)

        # If we've just inserted blocks for a file, then next time we see
        # a file, it's id should be one greater than it is now.
        if char_is_file:
            file_id += 1

        # The Disk Map alternates between file ids and empty space.
        char_is_file = not char_is_file

    return disk_expanded

def compact_disk(disk_expanded):
    disk_compacted = disk_expanded[:]

    space_ptr = 0
    file_block_ptr = len(disk_compacted) - 1

    while space_ptr < file_block_ptr:
        while disk_compacted[space_ptr] != EMPTY_SPACE and space_ptr < file_block_ptr:
            space_ptr += 1

        while disk_compacted[file_block_ptr] == EMPTY_SPACE and space_ptr < file_block_ptr:
            file_block_ptr -= 1

        if space_ptr < file_block_ptr:
            disk_compacted[space_ptr], disk_compacted[file_block_ptr] = \
                disk_compacted[file_block_ptr], disk_compacted[space_ptr]

    return disk_compacted

def calculate_checksum(disk_compacted):
    checksum = 0

    for i, file_id in enumerate(disk_compacted):
        if file_id != EMPTY_SPACE:
            checksum += i * file_id

    return checksum

def compact_blocks(filename):
    disk_map = get_disk_map_from_file(filename)
    disk_expanded = expand_disk_map(disk_map)

    disk_compacted = compact_disk(disk_expanded)

    checksum = calculate_checksum(disk_compacted)
    return checksum

if __name__ == "__main__":
    print(compact_blocks(FILENAME))
