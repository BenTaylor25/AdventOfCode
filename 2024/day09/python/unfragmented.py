from compact_blocks import *

BACKWARDS = -1
FOREWARDS = 1

def get_idx_of_other_side(disk_compacted, idx, dir):
    other_idx = idx

    char = disk_compacted[other_idx]

    while disk_compacted[other_idx + dir] == char:
        other_idx += dir

    return other_idx

def compact_disk(disk_expanded):
    disk_compacted = disk_expanded[:]

    space_ptr_a = 0
    space_ptr_b = 0

    file_block_ptr_a = len(disk_compacted) - 1
    file_block_ptr_b = len(disk_compacted) - 1

    while file_block_ptr_b > 0:
        while disk_compacted[file_block_ptr_b] == EMPTY_SPACE and space_ptr_a < file_block_ptr_b:
            file_block_ptr_b -= 1

        file_block_ptr_a = get_idx_of_other_side(disk_compacted, file_block_ptr_b, BACKWARDS)
        file_block_size = file_block_ptr_b - file_block_ptr_a + 1

        # print(file_block_ptr_a, file_block_ptr_b, file_block_size)

        space_ptr_a = 0
        space_ptr_b = 0

        space_too_small = True

        while space_too_small and space_ptr_a < file_block_ptr_b:
            while disk_compacted[space_ptr_a] != EMPTY_SPACE and space_ptr_a < file_block_ptr_b:
                space_ptr_a += 1

            space_ptr_b = get_idx_of_other_side(disk_compacted, space_ptr_a, FOREWARDS)
            space_size = space_ptr_b - space_ptr_a + 1

            space_too_small = space_size < file_block_size
            if space_too_small:
                space_ptr_a += 1

        if not space_too_small and space_ptr_a < file_block_ptr_b:
            file_char = disk_compacted[file_block_ptr_a]

            if file_char == 8:
                print(f"file_char 8 : {space_size}, {file_block_size}")

            for i in range(file_block_size):
                disk_compacted[file_block_ptr_a + i] = EMPTY_SPACE
                disk_compacted[space_ptr_a + i] = file_char
        else:
            file_block_ptr_b -= file_block_size

    return disk_compacted


# Python hack to overwrite function.
import compact_blocks
compact_blocks.compact_disk = compact_disk

if __name__ == "__main__":
    print(compact_blocks.compact_blocks(FILENAME))
