from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error

class Day10Part1:
    puzzle = None

    def run(self):
        adapters = self.parsed_input
        used_adapters = self.sort_adapters(adapters)
        differences = self.find_joltage_differences(used_adapters)
        one_diff = len(differences[0]) + 1
        three_diff = len(differences[2]) + 1
        print(one_diff * three_diff)

    def sort_adapters(self, adapters):
        return sorted(adapters)

    def find_joltage_differences(self, adapters):
        diffs = [[],[],[]]
        for i, curr_adapter in enumerate(adapters):
            if i == len(adapters)-1: break
            next_adapter = adapters[i+1]
            diff = next_adapter - curr_adapter
            diffs[diff-1].append(next_adapter)
        return diffs

    @cached_property
    def parsed_input(self):
        return [int(line.strip('\n')) for line in self.puzzle.input]
    