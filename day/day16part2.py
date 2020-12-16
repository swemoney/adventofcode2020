from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from collections import deque
from enum import Enum, auto
from functools import reduce
import math

class InputSection(Enum):
    rules = "rules"
    my_ticket = "your ticket:"
    nearby_tickets = "nearby tickets:"

class Day16Part2:
    puzzle = None

    def run(self):
        self.rules, self.my_ticket, self.all_tickets = self.parsed_input
        valid_tickets = [ticket for ticket in self.all_tickets if self.is_ticket_valid(ticket, self.rules)]
        possible_rules = self.test_rules_against_fields(valid_tickets, self.rules)
        rules_done = self.match_fields_to_rules(possible_rules)
        print(rules_done)

        relevant_data = []
        relevant_data.append(self.my_ticket[0][rules_done['departure location']])
        relevant_data.append(self.my_ticket[0][rules_done['departure date']])
        relevant_data.append(self.my_ticket[0][rules_done['departure station']])
        relevant_data.append(self.my_ticket[0][rules_done['departure platform']])
        relevant_data.append(self.my_ticket[0][rules_done['departure time']])
        relevant_data.append(self.my_ticket[0][rules_done['departure track']])
        print(math.prod(relevant_data))

    def match_fields_to_rules(self, possible_rules):
        rules_done = {}
        num_matches = 1
        while num_matches <= len(possible_rules):
            for f in possible_rules:
                if len(possible_rules[f]) == num_matches and f not in rules_done.values():
                    for rule_name in possible_rules[f]:
                        if rule_name not in rules_done:
                            rules_done[rule_name] = f
                    break
            num_matches += 1
        return rules_done

    def test_rules_against_fields(self, tickets, rules):
        field_rules = {}
        for f in range(len(self.my_ticket[0])):
            field_rules[f] = []
            for rule_name in rules:
                field_data = [ticket[f] for ticket in tickets]
                valid_tickets = list(filter(lambda v: self.passes_rule(v, rules[rule_name]), field_data))
                if len(valid_tickets) == len(tickets): field_rules[f].append(rule_name)
        return field_rules
                
    def passes_rule(self, val, rule):
        return val in rule[0] or val in rule[1]

    def is_ticket_valid(self, ticket, rules):
        for val in ticket:
            if not self.passes_rules(val, rules): return False
        return True

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

        return (parsed[InputSection.rules], parsed[InputSection.my_ticket], parsed[InputSection.nearby_tickets])
    