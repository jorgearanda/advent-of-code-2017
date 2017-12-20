lines = [x.replace(':', '').split() for x in open('inputs/d13-input.txt', 'r').readlines()]
scanners = {int(x[0]): int(x[1]) for x in lines}


def run(delay):
    severity = 0
    pico = delay
    for i in range(100):
        if i in scanners:
            depth = scanners[i]
            if pico % ((depth - 1) * 2) == 0:
                severity += pico * depth
        pico += 1

    return severity

print('Part 1:', run(0))

i = 0
while True:
    if run(i) == 0:
        print('Part 2:', i)
        break
    i += 1
