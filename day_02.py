def clean_division(x1, x2):
    """Checks if there is a way to divide the parameters without modulo, and if so, returns the result as well."""
    if (x1 / x2 % 1) == 0:
        return True, int(x1 / x2)
    if (x2 / x1 % 1) == 0:
        return True, int(x2 / x1)
    return False, None


rows = [[int(y) for y in x.split()] for x in open('inputs/d02-input.txt', 'r').readlines()]

checksum = 0
divisible_sum = 0
for row in rows:
    checksum += max(row) - min(row)
    for i in range(len(row) - 1):
        for j in range(i + 1, len(row)):
            is_clean, division = clean_division(row[i], row[j])
            if is_clean:
                divisible_sum += division
                break

print('Part 1:', checksum)
print('Part 2:', divisible_sum)
