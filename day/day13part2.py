from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error

class Day13Part2:
    puzzle = None

    def run(self):
        busses = self.parsed_input
        print(self.find_timestamp(busses))

    def find_timestamp(self, busses):
        divs = [bus for bus in busses if bus != 'x']
        rems = [bus - minute for minute,bus in enumerate(busses) if bus != 'x']
        return chinese_remainder(divs, rems)

    @cached_property
    def parsed_input(self):
        busses =  [b for b in self.puzzle.input[1].strip('\n').split(',')]
        return list(map(lambda bus: bus if bus == "x" else int(bus), busses))

# Stole these functions since I have no idea how this math works.
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
