first_start = 512
second_start = 191
first_factor = 16807
second_factor = 48271
modulo = 2147483647
first_multiple = 4
second_multiple = 8


def match(first, second):
    return bin(first)[2:].zfill(32)[16:] == bin(second)[2:].zfill(32)[16:]


def cycle(first, second):
    global first_factor
    global second_factor
    global modulo

    new_first = (first * first_factor) % modulo
    new_second = (second * second_factor) % modulo

    return new_first, new_second


def discriminating_cycle(first, second):
    global first_factor
    global second_factor
    global modulo
    global first_multiple
    global second_multiple

    new_first = (first * first_factor) % modulo
    while new_first % first_multiple != 0:
        new_first = (new_first * first_factor) % modulo

    new_second = (second * second_factor) % modulo
    while new_second % second_multiple != 0:
        new_second = (new_second * second_factor) % modulo

    return new_first, new_second


def first_part():
    global first_start
    global second_start

    first = first_start
    second = second_start
    count = 0
    for i in range(40000000):
        first, second = cycle(first, second)
        if match(first, second):
            count += 1

    print('Part 1:', count)


def second_part():
    global first_start
    global second_start

    first = first_start
    second = second_start
    count = 0
    for i in range(5000000):
        first, second = discriminating_cycle(first, second)
        if match(first, second):
            count += 1

    print('Part 2:', count)


first_part()
second_part()
