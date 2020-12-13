from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error

# Currently "works" for all test data but isn't capable of processing the full data set in a reasonable time

class Day13Part2:
    puzzle = None

    def run(self):
        busses = self.parsed_input
        print(self.check_schedule(busses))

    def check_schedule(self, busses):
        anchor_bus = busses[0]
        curr_time = anchor_bus
        while not self.busses_aligned(busses[1:], curr_time):
            curr_time += anchor_bus
        return curr_time

    def busses_aligned(self, busses, time):
        for minute,bus in enumerate(busses):
            if bus == "x" or (time + minute + 1) % bus == 0:
                continue
            return False
        return True

    @cached_property
    def parsed_input(self):
        busses =  [b for b in self.puzzle.input[1].strip('\n').split(',')]
        return list(map(lambda bus: bus if bus == "x" else int(bus), busses))
    