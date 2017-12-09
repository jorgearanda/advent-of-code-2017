digits = open('inputs/p01-input.txt', 'r').read().strip()
sum = 0
for i in range(-1, len(digits) - 1):
    if digits[i] == digits[i + 1]:
        sum += int(digits[i])

print(sum)
