from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error

class Seat:
    code: str
    row: int
    col: int
    sid: int

    def __init__(self, code):
        self.code = code
        self.row, self.col, self.sid = self.decode(code)

    def __str__(self):
        return f"Seat {self.code}: Row: {self.row}, Col: {self.col}, ID: {self.sid}"

    def decode(self, chars):
        row = self.decode_section(chars[:7])
        col = self.decode_section(chars[-3:])
        sid = (row * 8) + col
        return (int(row), int(col), int(sid))

    def decode_section(self, chars):
        mn, mx = (0,127) if len(chars) == 7 else (0,7)
        for c in chars:
            mn, mx = self.halve(mn, mx, c)
        return mn

    def halve(self, mn, mx, char):
        x = (mx - mn + 1) / 2
        if char == "F" or char == "L":
            return (mn, mn + x - 1)
        return (mn + x, mx)
    
class Day5Part2:
    puzzle = None

    def run(self):
        seats = list(Seat(code) for code in self.parsed_input)
        print(self.find_missing(seats))

    def find_missing(self, seats):
        min_id = min(seat.sid for seat in seats)
        max_id = max(seat.sid for seat in seats)
        seat_id_range = range(min_id, max_id + 1)
        seat_ids = list(map(lambda seat: seat.sid, seats))
        return list(filter(lambda seat_id: seat_id not in seat_ids, seat_id_range))

    @cached_property
    def parsed_input(self):
        return [code.replace('\n',"") for code in self.puzzle.input]
    