rows = [x.split() for x in open('inputs/d04-input.txt', 'r').readlines()]

no_repeats = 0
no_anagrams = 0
for row in rows:
    for i in range(len(row) - 1):
        if row[i] in row[i + 1:]:
            break
    else:
        no_repeats += 1

    letters = [[letter for letter in item] for item in row]
    for item in letters:
        item.sort()
    sorted_words = [''.join(item) for item in letters]

    for i in range(len(sorted_words) - 1):
        if sorted_words[i] in sorted_words[i + 1:]:
            break
    else:
        no_anagrams += 1

print('Part 1:', no_repeats)
print('Part 2:', no_anagrams)
