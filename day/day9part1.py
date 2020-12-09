from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from dataclasses import dataclass

@dataclass
class Result:
    x: int
    y: int
    sum_requested: int

class Day9Part1:
    puzzle = None

    def run(self):
        self.decode(self.parsed_input, 25)

    def decode(self, data, preamble):
        for i in range(preamble, len(data)):
            relevant_data = data[i-preamble:i+1]
            pair = self.find_pair_for_sum(relevant_data)
            if pair.x == None and pair.y == None:
                print(pair.sum_requested)
            
    def find_pair_for_sum(self, data):
        sum_requested = data[-1:][0]
        test_data = data[:-1]
        for x in test_data:
            for y in test_data:
                if x == y: continue
                if x + y == sum_requested:
                    return Result(x, y, sum_requested)
        return Result(None, None, sum_requested)

    @cached_property
    def parsed_input(self):
        return [int(line.strip('\n')) for line in self.puzzle.input]
    