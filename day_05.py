instructions = [int(x) for x in open('inputs/d05-input.txt', 'r').readlines()]

jumps = 0
idx = 0

while idx >= 0 and idx < len(instructions):
    old_idx = idx
    idx = idx + instructions[idx]
    instructions[old_idx] += 1
    jumps += 1

print('Part 1:', jumps)


instructions = [int(x) for x in open('inputs/d05-input.txt', 'r').readlines()]

jumps = 0
idx = 0

while idx >= 0 and idx < len(instructions):
    old_idx = idx
    idx = idx + instructions[idx]
    if instructions[old_idx] >= 3:
        instructions[old_idx] -= 1
    else:
        instructions[old_idx] += 1
    jumps += 1

print('Part 2:', jumps)
