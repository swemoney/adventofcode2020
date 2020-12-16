from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from collections import deque
from enum import Enum, auto

class InputSection(Enum):
    rules = "rules"
    my_ticket = "your ticket:"
    nearby_tickets = "nearby tickets:"

class Day16Part1:
    puzzle = None

    def run(self):
        input_data = self.parsed_input
        invalid_data = self.find_invalid_data(input_data[InputSection.nearby_tickets], input_data[InputSection.rules])
        print(sum(invalid_data))

    def find_invalid_data(self, tickets, rules):
        invalid_data = []
        for ticket in tickets:
            invalid_data.extend(self.invalid_ticket_data(ticket, rules))
        return invalid_data

    def invalid_ticket_data(self, ticket, rules):
        invalid_data = []
        for val in ticket:
            if not self.passes_rules(val, rules):
                invalid_data.append(val)
        return invalid_data

    def passes_rules(self, val, rules):
        for rule_name in rules:
            for rng in rules[rule_name]:
                if val in rng: return True
        return False

    @cached_property
    def parsed_input(self):
        cleaned_input = [line.strip('\n') for line in self.puzzle.input if line != '\n']
        current_section = InputSection.rules
        parsed = {InputSection.rules: {}, InputSection.my_ticket: [], InputSection.nearby_tickets: []}

        for line in cleaned_input:
            if line == InputSection.my_ticket.value:
                current_section = InputSection.my_ticket
                continue
            if line == InputSection.nearby_tickets.value:
                current_section = InputSection.nearby_tickets
                continue
            
            if current_section == InputSection.rules:
                rule_name = line.split(": ")[0]
                range_strings = line.split(": ")[1].split(" or ")
                data = [range(int(r.split("-")[0]), int(r.split("-")[1])+1) for r in range_strings]
                parsed[current_section][rule_name] = data

            else:
                parsed[current_section].append(list(map(int,line.split(","))))

        return parsed
    