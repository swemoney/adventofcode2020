from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error

class Day1Part2:
    puzzle = None

    def run(self):
        a, b, c = self.get_result(2020)
        print(a * b * c)

    def get_result(self, result):
        for i in self.parsed_input:
            for j in self.parsed_input:
                for k in self.parsed_input:
                    if i + j + k == result:
                        return (i, j, k)

    @cached_property
    def parsed_input(self):
        return [int(i) for i in self.puzzle.input]
    