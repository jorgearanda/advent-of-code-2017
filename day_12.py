lines = [y.replace(',', '').split() for y in open('inputs/d12-input.txt', 'r').readlines()]
progs = {int(x[0]): list(map(int, x[2:])) for x in lines}

visited = []
groups = []


def add_to_group(group, p):
    group.add(p)
    for node in progs[p]:
        if node not in visited:
            visited.append(node)
            add_to_group(group, node)

for i in range(2000):
    if i not in visited:
        groups.append(set())
        add_to_group(groups[-1], i)

print('Part 1:', len(groups[0]))
print('Part 2:', len(groups))
