from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from enum import Enum, auto
import numpy as np

class SeatStatus(Enum):
    occupied = "#"
    unoccupied = "L"
    floor = "."
    
class Seat:
    status: SeatStatus

    def __init__(self, seat_string):
        self.status = SeatStatus(seat_string)

    @property
    def flipped(self):
        if self.status == SeatStatus.unoccupied:
            return SeatStatus.occupied
        if self.status == SeatStatus.occupied:
            return SeatStatus.unoccupied
        return SeatStatus.floor

    @property
    def is_floor(self):
        return self.status == SeatStatus.floor

    @property
    def is_occupied(self):
        return self.status == SeatStatus.occupied

    @property
    def is_unoccupied(self):
        return self.status == SeatStatus.unoccupied

    def __eq__(self, other):
        return self.status == other.status

class SeatMap:
    def __init__(self, seat_map):
        self.seats = []
        for row in seat_map:
            self.seats.append([Seat(col) for col in row])

    @property
    def unoccupied_count(self):
        return sum([[seat.status for seat in row].count(SeatStatus.unoccupied) for row in self.seats])

    @property
    def occupied_count(self):
        return sum([[seat.status for seat in row].count(SeatStatus.occupied) for row in self.seats])

    def simulate_people(self):
        new_seats = []
        for row, row_seats in enumerate(self.seats):
            new_row = []
            for col, seat in enumerate(row_seats):
                new_seat = Seat(seat.flipped.value) if self.should_flip_seat(row,col) else seat
                new_row.append(new_seat)
            new_seats.append(new_row)
        if np.array_equal(self.seats, new_seats):
            return
        self.seats = new_seats
        self.simulate_people()

    def should_flip_seat(self, row, col):
        seat = self.seats[row][col]
        neighbors = self.neighbors(row, col)
        if seat.is_floor: return False
        if (seat.is_unoccupied) and (SeatStatus.occupied not in [n.status for n in neighbors]):
            return True
        if (seat.is_occupied) and ([n.status for n in neighbors].count(SeatStatus.occupied) >= 4):
            return True
        return False

    def neighbors(self, row, col):
        neighbors = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                n_row, n_col = (row + i, col + j)
                if i == 0 and j == 0: continue # Starting seat
                if n_row < 0 or n_col < 0: continue # Don't wrap around
                if n_row > len(self.seats)-1: continue # Out of bounds
                if n_col > len(self.seats[i])-1: continue # Out of bounds
                neighbors.append(self.seats[n_row][n_col])
        return neighbors

class Day11Part1:
    puzzle = None

    def run(self):
        seat_map = SeatMap(self.parsed_input)
        seat_map.simulate_people()
        print(seat_map.occupied_count)

    @cached_property
    def parsed_input(self):
        return [list(line.strip('\n')) for line in self.puzzle.input]
    