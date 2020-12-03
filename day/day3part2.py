from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
import math
from dataclasses import dataclass

@dataclass
class Slope:
    right: int
    down: int
    full_map: [str]

class Day3Part2:
    puzzle = None

    def run(self):
        slopes = [
            Slope(1, 1, self.parsed_input(1)),
            Slope(3, 1, self.parsed_input(3)),
            Slope(5, 1, self.parsed_input(5)),
            Slope(7, 1, self.parsed_input(7)),
            Slope(1, 2, self.parsed_input(1))]
        trees = []
        for slope in slopes:
            trees.append(self.count_trees_on_slope(slope))
        print(math.prod(trees))

    def count_trees_on_slope(self, slope: Slope):
        y = 0
        x = 0
        trees = 0

        while (y + slope.down) <= len(slope.full_map) - 1:
            y += slope.down
            x += slope.right

            if slope.full_map[y][x] == "#":
                trees += 1
        return trees

    def parsed_input(self, right):
        full_map = []
        number_of_lines = len(self.puzzle.input)
        for line in self.puzzle.input:
            l = line.replace('\n','')
            full_map.append(l * (right + 1) * number_of_lines)
        return full_map
    