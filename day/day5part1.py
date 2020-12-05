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

class Day5Part1:
    puzzle = None

    def run(self):
        seats = list(Seat(code) for code in self.parsed_input)
        print(max(seat.sid for seat in seats))

    @cached_property
    def parsed_input(self):
        return [code.replace('\n',"") for code in self.puzzle.input]
    