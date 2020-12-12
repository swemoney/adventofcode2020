from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from enum import Enum
from dataclasses import dataclass

class Direction(Enum):
    forward = "F"
    left = "L"
    right = "R"
    north = "N"
    south = "S"
    west = "W"
    east = "E"

    @classmethod
    def deg_to_compass(c, deg: int):
        return [c.north, c.east, c.south, c.west][int(deg/90) % 4]

    @classmethod
    def dir_to_deg(c, dir):
        if dir == c.north: return 0
        elif dir == c.east: return 90
        elif dir == c.south: return 180
        elif dir == c.west: return 270
        return None

    @classmethod
    def turn(c, start_d, turn_d, amount):
        deg = c.dir_to_deg(start_d)
        deg += amount * (1 if turn_d == Direction.right else -1)
        return c.deg_to_compass(deg)

    @classmethod
    def movement(c, facing):
        if facing == c.north: return (1, 0)
        if facing == c.south: return (-1, 0)
        if facing == c.east:  return (0, 1)
        if facing == c.west:  return (0, -1)
        return (0, 0)


@dataclass
class Position:
    y: int
    x: int
    facing: Direction

    def turn(self, inst):
        self.facing = Direction.turn(self.facing, inst.direction, inst.amount)

    def move(self, inst):
        d = inst.direction
        if inst.direction == Direction.forward:
            d = self.facing
        my, mx = Direction.movement(d)
        self.y += my * inst.amount
        self.x += mx * inst.amount

    def manhattan(self, orig_x=0, orig_y=0):
        return abs(self.x - orig_x) + abs(self.y - orig_y)

    def __str__(self):
        s = "East " if self.x >= 0 else "West "
        s += str(abs(self.x)) + ", "
        s += "North " if self.y >= 0 else "South "
        s += str(abs(self.y))
        return s

class Instruction:
    direction: Direction
    amount: int

    def __init__(self, instruction: str):
        self.direction = Direction(instruction[0])
        self.amount = int(instruction[1:])

    def movement(self, facing):
        if self.direction == Direction.north: return (0, 1)
        if self.direction == Direction.south: return (0, -1)
        if self.direction == Direction.east:  return (1, 0)
        if self.direction == Direction.west:  return (-1, 0)
        return (0, 0)

class Navigator:
    def __init__(self, instructions: [Instruction]):
        self.instructions = instructions
        self.position = Position(0, 0, Direction.east)

    def run_instructions(self):
        for inst in self.instructions:
            self.execute_instruction(inst)

    def execute_instruction(self, inst: Instruction):
        d = inst.direction
        if d in [Direction.right, Direction.left]:
            return self.position.turn(inst)
        return self.position.move(inst)

class Day12Part1:
    puzzle = None

    def run(self):
        instructions = [Instruction(inst) for inst in self.parsed_input]
        navigator = Navigator(instructions)
        navigator.run_instructions()
        print(navigator.position)
        print(navigator.position.manhattan())

    @cached_property
    def parsed_input(self):
        return [line.strip('\n') for line in self.puzzle.input]
    