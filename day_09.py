stream = open('inputs/d09-input.txt', 'r').read()

score = 0
depth = 0
garbage = 0
state = 'group'  # or garbage, or bang

for char in stream:
    if state == 'group':
        if char == '{':
            depth += 1
            score += depth
        elif char == '}':
            depth -= 1
        elif char == '<':
            state = 'garbage'
    elif state == 'garbage':
        if char == '>':
            state = 'group'
        elif char == '!':
            state = 'bang'
        else:
            garbage += 1
    else:  # bang
        state = 'garbage'

print('Part 1:', score)
print('Part 2:', garbage)
