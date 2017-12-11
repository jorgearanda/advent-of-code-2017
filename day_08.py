instructions = [x.split() for x in open('inputs/d08-input.txt', 'r').readlines()]
registers = {x[0]: 0 for x in instructions}
max_ever = 0

for instruction in instructions:
    target = instruction[0]
    value = int(instruction[2])
    if instruction[1] == 'dec':
        value = -value
    operand = instruction[4]
    operator = instruction[5]
    comparison = int(instruction[6])

    operand_value = registers[operand]
    if (operator == '==' and operand_value == comparison) or \
            (operator == '>' and operand_value > comparison) or \
            (operator == '>=' and operand_value >= comparison) or \
            (operator == '<' and operand_value < comparison) or \
            (operator == '<=' and operand_value <= comparison) or \
            (operator == '!=' and operand_value != comparison):
        registers[target] += value

    max_ever = max(max_ever, registers[target])

print('Part 1:', registers[max(registers, key=registers.get)])
print('Part 2:', max_ever)
