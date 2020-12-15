from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error

class Day15Part1:
    puzzle = None

    def run(self):
        start_nums = self.parsed_input
        number_spoken = self.play_game(start_nums, 2020)
        print(number_spoken)

    def play_game(self, start_nums, goal_rounds):
        rounds = start_nums
        for round_num in range(len(start_nums)+1, goal_rounds+1):
            last_num = rounds[-1]
            if rounds.count(last_num) == 1:
                rounds.append(0)
            else:
                 last_appeared = len(rounds) - list(reversed(rounds[:-1])).index(last_num) - 1
                 rounds.append(round_num-1 - last_appeared)
        return rounds[-1]

    @cached_property
    def parsed_input(self):
        return [int(start_num) for start_num in self.puzzle.input[0].strip('\n').split(",")]
    