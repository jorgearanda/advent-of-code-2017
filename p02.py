digits = open('inputs/p01-input.txt', 'r').read().strip()
sum = 0
step = len(digits) / 2
for i in range(-1, len(digits) - 1):
    if digits[i] == digits[int((i + step) % len(digits))]:
        sum += int(digits[i])

print(sum)
