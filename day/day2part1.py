from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from dataclasses import dataclass

@dataclass
class Policy:
    character: str
    minimum: int
    maximum: int

@dataclass
class Password:
    password: str
    policy: Policy

class Day2Part1:
    puzzle = None

    def run(self):
        valid_passwords = self.get_valid_passwords()
        print(len(valid_passwords))

    def get_valid_passwords(self):
        valid_passwords = []
        for password in self.parsed_input:
            if self.is_valid_password(password):
                valid_passwords.append(password)
        return valid_passwords

    def is_valid_password(self, p: Password):
        count = p.password.count(p.policy.character)
        return p.policy.minimum <= count <= p.policy.maximum

    @cached_property
    def parsed_input(self):
        passwords = []
        for pass_policy in self.puzzle.input:
            s = pass_policy.split(" ")
            password = s[2].replace('\n',"")
            character = s[1].replace(":","")
            minimum = int(s[0].split("-")[0])
            maximum = int(s[0].split("-")[1])
            passwords.append( Password(password, Policy(character, minimum, maximum)) )
        return passwords
