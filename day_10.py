lengths = [int(x) for x in open('inputs/d10-input.txt', 'r').read().strip().split(',')]
ascii_lengths = [ord(x) for x in open('inputs/d10-input.txt', 'r').read().strip()]
ascii_lengths = ascii_lengths + [17, 31, 73, 47, 23]
string = [x for x in range(256)]


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


part1, _, _ = knot_hash_cycle(string, lengths)
print('Part 1:', part1[0] * part1[1])

string = [x for x in range(256)]
print('Part 2:', knot_hash(string, ascii_lengths))
