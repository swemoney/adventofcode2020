from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from dataclasses import dataclass

PASSPORT_FIELDS = {
    "byr": "birth_year",
    "iyr": "issue_year",
    "eyr": "expire_year",
    "hgt": "height",
    "ecl": "eye_color",
    "hcl": "hair_color",
    "pid": "passport_id",
    "cid": "country_id"}

class Passport:
    birth_year: int   # byr
    issue_year: int   # iyr
    expire_year: int  # eyr
    height: str       # hgt
    eye_color: str    # ecl
    hair_color: str   # hcl
    passport_id: int  # pid
    country_id: int   # cid

    def is_valid(self):
        if len(vars(self)) < 7:
            return False
        if len(vars(self)) == 8:
            return True
        if vars(self).get("country_id") == None:
            return True
        return False

class Day4Part1:
    puzzle = None

    def run(self):
        passports = self.parsed_input
        valid_passports = []
        for p in passports:
            if p.is_valid():
                valid_passports.append(p)
        print(len(valid_passports))
        
    @cached_property
    def parsed_input(self):
        passports = []
        i = 0
        passport_data = []
        while i <= len(self.puzzle.input):
            passport_data.append(self.puzzle.input[i].replace('\n',""))
            i += 1
            if i >= len(self.puzzle.input) or self.puzzle.input[i] == '\n':
                passport = Passport()
                for data_line in passport_data:
                    for d in data_line.split(" "):
                        setattr(passport, PASSPORT_FIELDS[d.split(":")[0]], d.split(":")[1])
                passports.append(passport)
                passport_data = []
                i += 1
        return passports
    