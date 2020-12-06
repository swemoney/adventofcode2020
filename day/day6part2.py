from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error

class Day6Part2:
    puzzle = None

    def run(self):
        groups = [self.find_common(list(group)) for group in self.parsed_input]
        group_yes = [len(group) for group in groups]
        print(sum(group_yes))

    def find_common(self, groups):
        return set.intersection(*map(set, groups))

    @cached_property
    def parsed_input(self):
        joined = "".join(self.puzzle.input) # Re-join the input into a single string
        groups = [group.split('\n') for group in joined.split("\n\n")]
        return [" ".join(group).split() for group in groups] # Remove blanks
    