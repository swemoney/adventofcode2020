from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from collections import defaultdict
import time

class Day15Part2:
    puzzle = None

    def run(self):
        start_nums = self.parsed_input
        start_time = time.time()
        print(self.play_game(start_nums, 30000000))
        print(time.time() - start_time)

    def play_game(self, start_nums, goal_rounds):
        spoken_nums = {}
        curr_num, next_num = 0, 0
        for r, n in enumerate(start_nums):
            spoken_nums[n] = r + 1
            curr_num, next_num = n, 0

        curr_round = len(start_nums) + 1
        while curr_round <= goal_rounds:
            curr_num = next_num
            next_num = curr_round - spoken_nums[curr_num] if curr_num in spoken_nums else 0
            spoken_nums[curr_num] = curr_round
            curr_round += 1
        return curr_num

    @cached_property
    def parsed_input(self):
        return [int(start_num) for start_num in self.puzzle.input[0].strip('\n').split(",")]
    