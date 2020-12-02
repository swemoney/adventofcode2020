from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from dataclasses import dataclass

@dataclass
class Policy:
    character: str
    positions: [int]

@dataclass
class Password:
    password: str
    policy: Policy

class Day2Part2:
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
        pos = p.policy.positions
        return (p.password[pos[0] - 1] == p.policy.character) ^ (p.password[pos[1] - 1] == p.policy.character)

    @cached_property
    def parsed_input(self):
        passwords = []
        for pass_policy in self.puzzle.input:
            s = pass_policy.split(" ")
            password = s[2].replace('\n',"")
            character = s[1].replace(":","")
            positions = [int(i) for i in s[0].split("-")]
            passwords.append( Password(password, Policy(character, positions)) )
        return passwords
