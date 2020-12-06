from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error

class Day6Part1:
    puzzle = None

    def run(self):
        groups = [self.remove_dupliates(group) for group in self.parsed_input]
        group_yes = [len(group) for group in groups]
        print(sum(group_yes))

    def remove_dupliates(self, l):
        return list(dict.fromkeys(l))

    @cached_property
    def parsed_input(self):
        joined = "".join(self.puzzle.input) # Re-join the input into a single string
        groups = joined.split("\n\n")       # Split by \n\n to get each group
        return [person.replace('\n',"") for person in groups] # remove extra new lines
    