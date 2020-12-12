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
    def movement(c, facing):
        if facing == c.north: return (0, 1)
        if facing == c.south: return (0, -1)
        if facing == c.east:  return (1, 0)
        if facing == c.west:  return (-1, 0)
        return (0, 0)

@dataclass
class Position:
    x: int
    y: int
    facing: Direction

    def turn(self, inst):
        x, y = self.x, self.y
        deg = 360 - inst.amount if inst.direction == Direction.left else inst.amount
        rotated = {90: (y, -x), 180: (-x, -y), 270: (-y, x)}
        self.x, self.y = rotated[deg]
        return self

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

class Navigator:
    def __init__(self, instructions: [Instruction]):
        self.instructions = instructions
        self.position = Position(0, 0, Direction.east)
        self.waypoint = Position(10, 1, Direction.east)

    def run_instructions(self):
        for inst in self.instructions:
            self.execute_instruction(inst)

    def execute_instruction(self, inst: Instruction):
        d = inst.direction
        if d in [Direction.right, Direction.left]:
            return self.waypoint.turn(inst)
        if d == Direction.forward:
            return self.move_ship(inst)
        return self.move_waypoint(inst)

    def move_ship(self, inst):
        mx, my = (self.waypoint.x, self.waypoint.y)
        self.position.x += mx * inst.amount
        self.position.y += my * inst.amount
        return self.position

    def move_waypoint(self, inst):
        d = inst.direction
        mx, my = Direction.movement(d)
        self.waypoint.x += mx * inst.amount
        self.waypoint.y += my * inst.amount
        return self.waypoint

class Day12Part2:
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
    