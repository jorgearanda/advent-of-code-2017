digits = [int(x) for x in open('inputs/p01-input.txt', 'r').read().strip()]


def calc(step):
    global digits
    total = 0
    for idx in range(len(digits)):
        compare_idx = int((idx + step) % len(digits))
        if digits[idx] == digits[compare_idx]:
            total += digits[idx]

    return total


print('Part 1:', calc(1))
print('Part 2:', calc(len(digits) / 2))
