from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
import operator
import re

ops = {'+': operator.add, '*': operator.mul}

class Day18Part1:
    puzzle = None

    def run(self):
        answers = [self.parse_problem(problem) for problem in self.parsed_input]
        print(sum(answers))

    def parse_problem(self, problem_string):
        special = ['+','*','(',')']
        stripped = re.compile(r'\S').findall(problem_string)
        parts, stack = [], []
        for c in stripped:
            if c == "(":
                stack.append(c)
                continue

            if c == ")":
                inner = []
                stk = stack.pop()
                while stk != "(":
                    inner.append(stk if stk in special else int(stk))
                    stk = stack.pop()
                inner_eval = self.evaluate(inner)
                if len(stack) > 0:
                    stack.append(inner_eval)
                else:
                    parts.append(inner_eval)
                continue

            if len(stack) == 0:
                parts.append(c if c in special else int(c))
            else:
                stack.append(c)

        return self.evaluate(list(reversed(parts)))

    def evaluate(self, problem):
        curr_val = 0
        while len(problem) > 0:
            part = problem.pop()
            if part in ops:
                next_val = problem.pop()
                curr_val = ops[part](curr_val, next_val)
            else: curr_val = part
        return curr_val

    @cached_property
    def parsed_input(self):
        return [line.strip('\n') for line in self.puzzle.input]
