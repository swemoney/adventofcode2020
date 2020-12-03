from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
import math

class Day3Part1:
    puzzle = None
    side_movement = 3
    down_movement = 1

    def run(self):
        print(self.count_trees_on_slope())
        
    def count_trees_on_slope(self):
        y = 0
        x = 0
        trees = 0

        while y < len(self.parsed_input) - 1:
            y += self.down_movement
            x += self.side_movement
            if self.parsed_input[y][x] == "#":
                trees += 1
        return trees

    @cached_property
    def parsed_input(self):
        number_of_lines = len(self.puzzle.input)
        full_map = []
        for line in self.puzzle.input:
            l = line.replace('\n','')
            l_len = len(l)
            w = int(l_len / self.side_movement)
            full_map.append(l * math.ceil(w * number_of_lines / l_len))
        return full_map
    