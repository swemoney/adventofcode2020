from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
import math

class Day13Part1:
    puzzle = None

    def run(self):
        earliest, busses = self.parsed_input
        schedule = self.calculate_departures(busses, earliest)
        best_bus = self.find_best_bus(schedule, earliest)
        print(best_bus)
        print(math.prod(best_bus))

    def calculate_departures(self, busses, until):
        bus_schedule = {}
        for bus in busses:
            departure_time = bus
            departure_times = [bus]
            while departure_time < until:
                departure_time += bus
                departure_times.append(departure_time)
            bus_schedule[bus] = departure_times
        return bus_schedule

    def find_best_bus(self, schedule, earliest_departure):
        best = (-1, -1)
        for bus in schedule:
            wait_time = schedule[bus][-1] - earliest_departure
            if best == (-1,-1) or best[1] > wait_time:
                best = (bus, wait_time)
        return best

    @cached_property
    def parsed_input(self):
        earliest_departure = self.puzzle.input[0].strip('\n')
        all_busses = [b for b in self.puzzle.input[1].strip('\n').split(',')]
        active_busses = list(filter(lambda bus: bus != 'x', all_busses))
        return ( int(earliest_departure), list(map(int, active_busses)) )
    