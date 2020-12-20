from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error

class Day19Part2:
    puzzle = None

    def run(self):
        self.rules, messages = self.parsed_input
        print(sum([self.match('0', message) for message in messages]))

    def match(self, rule_id, message):
        return any(m == '' for m in self.traverse_rule(rule_id, message))

    def traverse_rule(self, rule_id, message):
        if isinstance(self.rules[rule_id], list):
            yield from self.traverse_expand(self.rules[rule_id], message)
        else:
            if message and message[0] == self.rules[rule_id]:
                yield message[1:]

    def traverse_expand(self, rule_list, message):
        for new_rule_list in rule_list:
            yield from self.check(new_rule_list, message)

    def check(self, rule_list, message):
        if not rule_list: yield message
        else:
            i, *rule_list = rule_list
            for message in self.traverse_rule(i, message):
                yield from self.check(rule_list, message)

    @cached_property
    def parsed_input(self):
        all_input = [line.strip() for line in self.puzzle.input]
        separator = all_input.index('')
        messages = all_input[separator+1:]
        rules = {}
        for rule in all_input[:separator]:
            rule_id = rule.split(": ")[0]
            rule_contents = rule.split(": ")[1]
            if '"' in rule_contents:
                rules[rule_id] = rule_contents.replace('"','')
            else:
                rule_ids = rule_contents.split(" ")
                if '|' in rule_ids:
                    pipe_idx = rule_ids.index('|')
                    rules[rule_id] = [list(rule_ids[:pipe_idx]), list(rule_ids[pipe_idx+1:])]
                else:
                    rules[rule_id] = [list(rule_ids)]
        return (self.fix_rules(rules), messages)

    def fix_rules(self, rules):
        rules['8'] =  [['42'], ['42','8']]
        rules['11'] = [['42','31'],['42','11','31']]
        return rules
