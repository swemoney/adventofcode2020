from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from dataclasses import dataclass
import re

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
        for key in vars(self):
            if getattr(self, f"{key}_valid")() == False:
                print(f"Validation Failed: {key} = {getattr(self, key)}")
                return False
        return True

    def has_all_valid_fields(self):
        if len(vars(self)) < 7:
            return False
        if len(vars(self)) == 8:
            return True
        if vars(self).get("country_id") == None:
            return True
        return False
        
    def birth_year_valid(self):
        year = int(self.birth_year)
        return 1920 <= year <= 2002

    def issue_year_valid(self):
        year = int(self.issue_year)
        return 2010 <= year <= 2020

    def expire_year_valid(self):
        year = int(self.expire_year)
        return 2020 <= year <= 2030

    def height_valid(self):
        u = self.height[-2:]
        h = int(self.height[:-2])
        if u == "in":
            return 59 <= h <= 76
        if u == "cm":
            return 150 <= h <= 193
        return False

    def eye_color_valid(self):
        return self.eye_color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def hair_color_valid(self):
        hair_color_match = re.match(r"^#[a-fA-F0-9]{6}$", self.hair_color)
        if hair_color_match == None:
            return False
        return True

    def passport_id_valid(self):
        passport_id_match = re.search(r"[0-9]{9}", self.passport_id)
        return passport_id_match != None

    def country_id_valid(self):
        return True

class Day4Part2:
    puzzle = None

    def run(self):
        passports = self.parsed_input
        valid_field_passports = []
        for p in passports:
            if p.has_all_valid_fields():
                valid_field_passports.append(p)
        print(len(valid_field_passports))

        valid_passports = []
        for p in valid_field_passports:
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
    