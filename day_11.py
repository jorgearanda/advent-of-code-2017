steps = open('inputs/d11-input.txt', 'r').read().strip().split(',')

dx = 0
dy = 0
dz = 0

maxdx = 0
maxdy = 0
maxdz = 0

for step in steps:
    if step == 'ne':
        dx += 1
        dz -= 1
    elif step == 'sw':
        dx -= 1
        dz += 1
    elif step == 'n':
        dy += 1
        dz -= 1
    elif step == 's':
        dy -= 1
        dz += 1
    elif step == 'nw':
        dy += 1
        dx -= 1
    elif step == 'se':
        dy -= 1
        dx += 1

    maxdx = max(maxdx, abs(dx))
    maxdy = max(maxdy, abs(dy))
    maxdz = max(maxdz, abs(dz))

print('Part 1:', max(abs(dx), abs(dy), abs(dz)))
print('Part 2:', max(maxdx, maxdy, maxdz))
