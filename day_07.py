nodes_list = [x.split() for x in open('inputs/d07-input.txt', 'r').readlines()]
nodes = [x[0] for x in nodes_list]

for branches in nodes_list:
    for branch in branches[2:]:
        stripped = branch.strip(',')
        if stripped in nodes:
            nodes.pop(nodes.index(stripped))

root = nodes[0]
print('Part 1:', root)

nodes = [x[0] for x in nodes_list]


class Node():
    def __init__(self, name):
        self.name = name
        node_data = nodes_list[nodes.index(name)]
        self.weight = int(node_data[1].strip('()'))
        self.own_weight = self.weight
        self.branches = []
        for branch_name in node_data[3:]:
            stripped = branch_name.strip(',')
            self.branches.append(Node(stripped))

        self.balanced = True
        if len(self.branches) > 1:
            first_weight = self.branches[0].weight
            for branch in self.branches:
                self.weight += branch.weight
                if branch.weight != first_weight:
                    self.balanced = False

        if not self.balanced:
            print('Tree imbalanced at', self.name)
            for branch in self.branches:
                print('  ', branch.name, branch.weight, branch.own_weight)
            print('---')

root_node = Node(root)
