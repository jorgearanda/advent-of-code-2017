base_input = 'xlqgujun'
# base_input = 'flqrgnkx'


def knot_hash_cycle(string, lengths, position=0, skip=0):
    for length in lengths:
        if length > 0:
            if position + length <= len(string):
                substring = string[position:position + length]
            else:
                substring = string[position:] + string[0:length - len(string[position:])]
            for item in substring[::-1]:
                string[position] = item
                position += 1
                if position >= len(string):
                    position = 0
        position += skip
        position = position % len(string)
        skip += 1

    return string, position, skip


def make_dense(string):
    dense_hash = ''
    for idx in range(16):
        block = string[idx * 16:idx * 16 + 16]
        hashed_block = 0
        for item in block:
            hashed_block = hashed_block ^ item
        dense_hash += ('0' + hex(hashed_block)[2:])[-2:]

    return dense_hash


def knot_hash(string, lengths):
    position = 0
    skip = 0
    for i in range(64):
        string, position, skip = knot_hash_cycle(string, lengths, position, skip)

    return make_dense(string)


def make_binary(hex_string):
    bin_string = ''
    for x in hex_string:
        bin_string += bin(int(x, 16))[2:].zfill(4)

    return bin_string


def prepare_input(base, idx):
    return base + '-' + str(idx)


def spill(i, j, value):
    global disk
    if disk[i][j] == '#':
        disk[i][j] = value
        if i > 0:
            spill(i - 1, j, value)
        if i < len(disk) - 1:
            spill(i + 1, j, value)
        if j > 0:
            spill(i, j - 1, value)
        if j < len(disk[i]) - 1:
            spill(i, j + 1, value)


disk = []
used = 0
for i in range(128):
    ascii_lengths = [ord(x) for x in prepare_input(base_input, i)]
    ascii_lengths = ascii_lengths + [17, 31, 73, 47, 23]
    string = [x for x in range(256)]
    row = make_binary(knot_hash(string, ascii_lengths))
    used += row.count('1')
    disk.append(list(row.replace('1', '#').replace('0', '.')))

print('Part 1:', used)

regions = 0
for i in range(128):
    for j in range(128):
        if disk[i][j] == '#':
            regions += 1
            spill(i, j, str(regions))

print('Part 2:', regions)
