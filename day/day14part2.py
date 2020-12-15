from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from itertools import product
from enum import Enum
import re

BIT_LENGTH = 36

class Command(Enum):
    mask = "mask"
    mem = "mem"

class Instruction:
    def __init__(self, command: str, address: str, argument: str):
        self.command = Command(command)
        self.address = None if address == None else int(address)
        self.argument = argument

class Day14Part2:
    puzzle = None

    def run(self):
        self.instructions = [self.parse_instruction(instruction_string) for instruction_string in self.parsed_input]
        self.memory = {0: 0}
        self.mask = "X" * BIT_LENGTH
        self.run_docking_program()
        print(sum(self.memory.values()))

    def run_docking_program(self):
        for instruction in self.instructions:
            self.execute_instruction(instruction)

    def execute_instruction(self, instruction):
        if instruction.command == Command.mask:
            self.mask = instruction.argument
        elif instruction.command == Command.mem:
            bin_string = self.int_to_bin(instruction.address)
            masked_addr = self.apply_mask(bin_string)
            for addr in self.expanded_floating_bits(masked_addr):
                self.memory[addr] = int(instruction.argument)

    def apply_mask(self, bit_string):
        bits = list(bit_string)
        for i, bit in enumerate(self.mask):
            if bit != "0": bits[i] = bit
        return "".join(bits)

    def expanded_floating_bits(self, masked_bits):
        all_bits = []
        indices = [i for i, c in enumerate(masked_bits) if c == "X"]
        for t in product("01", repeat=len(indices)):
            bits = list(masked_bits)
            for i, c in zip(indices, t):
                bits[i] = c
            all_bits.append(int("".join(bits),2))
        return all_bits

    def int_to_bin(self, integer):
        return bin(int(integer))[2:].zfill(BIT_LENGTH)

    def parse_instruction(self, instruction_string):
        instruction_parts = re.search(r"^(\w*)\[?(\d+)?\]?\s=\s(.*)$", instruction_string).groups()
        return Instruction(*instruction_parts)

    @cached_property
    def parsed_input(self):
        return [line.strip('\n') for line in self.puzzle.input]
    