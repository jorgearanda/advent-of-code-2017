import math
import numpy as np

input = int(open('inputs/d03-input.txt', 'r').read().strip())


class SpiralGrid():
    def __init__(self, size, target, style='inc'):
        self.side_size = size
        self.num_cells = int(size ** 2)
        self.grid = np.zeros(shape=(self.side_size, self.side_size))
        self.centre_x = int(self.side_size / 2)
        self.centre_y = self.centre_x
        self.target = target
        self.result = 0

        self._generate(style)

    def _generate(self, style):
        x = self.centre_x
        y = self.centre_y
        direction = 'east'
        populated = 0
        next_half_size = 0
        self.grid[x, y] = 1

        while populated < self.num_cells:
            populated += 1
            if style == 'inc':
                self.grid[x, y] = populated
                if populated == self.target:
                    self.result = abs(x - self.centre_x) + abs(y - self.centre_y)
                    break
            elif style == 'add':
                self.grid[x, y] = self._add_around(x, y)
                if self.grid[x, y] > self.target:
                    self.result = int(self.grid[x, y])
                    break

            if self._is_odd_root(populated):
                next_half_size += 1

            if direction == 'south' and x == self.centre_x + next_half_size:
                direction = 'east'
            elif direction == 'west' and y == self.centre_y - next_half_size:
                direction = 'south'
            elif direction == 'north' and x == self.centre_x - next_half_size:
                direction = 'west'
            elif direction == 'east' and y == self.centre_y + next_half_size:
                direction = 'north'

            if direction == 'north':
                x -= 1
            elif direction == 'west':
                y -= 1
            elif direction == 'south':
                x += 1
            else:
                y += 1

    def _is_odd_root(self, value):
        root = math.sqrt(value)
        return (root % 1) == 0 and (root % 2) == 1

    def _add_around(self, x, y):
        return np.sum(self.grid[x - 1:x + 2, y - 1:y + 2])


s = SpiralGrid(int(math.sqrt(input)) + 2, input)
print('Part 1:', s.result)

t = SpiralGrid(11, input, style='add')
print('Part 2:', t.result)
