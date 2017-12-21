steps = open('inputs/d16-input.txt', 'r').read().strip().split(',')
sequence = 'abcdefghijklmnop'


def spin(step, seq):
    amount = int(step[1:])
    return seq[-amount:] + seq[:-amount]


def exchange(step, seq):
    positions = [int(x) for x in step[1:].split('/')]
    value1 = seq[positions[0]]
    value2 = seq[positions[1]]
    seq = seq.replace(value1, 'x').replace(value2, value1).replace('x', value2)
    return seq


def partner(step, seq):
    programs = step[1:].split('/')
    seq = seq.replace(programs[0], 'x').replace(programs[1], programs[0]).replace('x', programs[1])
    return seq


def cycle(sequence):
    global steps
    for step in steps:
        if step[0] == 's':
            sequence = spin(step, sequence)
        elif step[0] == 'x':
            sequence = exchange(step, sequence)
        elif step[0] == 'p':
            sequence = partner(step, sequence)
        else:
            raise('Unknown type of step')

    return sequence

sequence = 'abcdefghijklmnop'
print('Part 1:', cycle(sequence))

sequence = 'abcdefghijklmnop'
for i in range(1000000):
    sequence = cycle(sequence)
    if sequence == 'abcdefghijklmnop':
        loop = i + 1
        break

remainder = 1000000000 % loop
sequence = 'abcdefghijklmnop'
for i in range(remainder):
    sequence = cycle(sequence)

print('Part 2:', sequence)
