blocks = [int(x) for x in open('inputs/d06-input.txt', 'r').read().split()]


class MemoryBank():
    def __init__(self, blocks):
        self.blocks = blocks
        self.cycles = 0
        self.history = []

    def redistribute(self):
        while str(self.blocks) not in self.history:
            self.history.append(str(self.blocks))
            self.cycle()

        print('Part 1:', self.cycles)
        print('Part 2:', self.cycles - self.history.index(str(self.blocks)))

    def cycle(self):
        from_idx = self._find_max()
        amount = self.blocks[from_idx]
        self.blocks[from_idx] = 0
        to_idx = (from_idx + 1) % len(self.blocks)

        while amount > 0:
            self.blocks[to_idx] += 1
            to_idx = (to_idx + 1) % len(self.blocks)
            amount -= 1

        self.cycles += 1

    def _find_max(self):
        max_value = max(self.blocks)
        return self.blocks.index(max_value)

m = MemoryBank(blocks)
m.redistribute()
