from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from enum import Enum

class Command:
    acc = "acc"
    jmp = "jmp"
    nop = "nop"

class Instruction:
    command: str
    argument: int

    def __init__(self, line):
        split = line.split(" ")
        self.command = split[0]
        self.argument = int(split[1])

    def __str__(self):
        return f"Instruction: {self.command}, {self.argument}"

class Day8Part1:
    puzzle = None

    def run(self):
        accumulator = self.run_program()
        print(accumulator)

    def run_program(self, start_on_line=1, accumulator_start=0):
        executed_lines = []
        line_number = start_on_line
        next_line = start_on_line
        accumulator = accumulator_start
        while line_number not in executed_lines:
            if next_line not in executed_lines:
                executed_lines.append(next_line)
            line_number, accumulator = self.run_line(line_number, accumulator)
            next_line = line_number
        return accumulator

    def run_line(self, line_number, accumulator):
        instruction = self.parsed_input[line_number - 1]
        if instruction.command == Command.acc:
            accumulator += instruction.argument
            return (line_number + 1, accumulator)
        elif instruction.command == Command.jmp:
            return (line_number + instruction.argument, accumulator)
        return (line_number + 1, accumulator)

    @cached_property
    def parsed_input(self):
        return [Instruction(line.strip('\n')) for line in self.puzzle.input]
    