from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from dataclasses import dataclass

@dataclass
class Result:
    x: int
    y: int
    sum_requested: int

class Day9Part2:
    puzzle = None

    def run(self):
        data = self.parsed_input
        weak_link = self.find_weak_link(data, 25)
        print(f"Weak Link: {weak_link}")
        num_list = self.find_list_of_nums(data, weak_link)
        print(f"Num List: {num_list}")
        result = min(num_list) + max(num_list)
        print(f"Result: {result}")

    def find_list_of_nums(self, data, weak_link):
        curr_start = 0
        while curr_start < len(data):
            curr_sum = 0
            for i, n in enumerate(data[curr_start:]):
                curr_sum += n
                if curr_sum == weak_link:
                    return data[curr_start:curr_start+i+1]
                if curr_sum > weak_link: break
            curr_start += 1

    def find_weak_link(self, data, preamble):
        for i in range(preamble, len(data)):
            relevant_data = data[i-preamble:i+1]
            pair = self.find_pair_for_sum(relevant_data)
            if pair.x == None and pair.y == None:
                return pair.sum_requested
            
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
    