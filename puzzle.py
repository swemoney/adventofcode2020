from functools import cached_property
from importlib import import_module

DAY_PATH = "day"
INPUT_PATH = "input"

class Puzzle:
    def __init__(self, day, part):
        self.day = day
        self.part = part

    @cached_property
    def day_filename(self):
        return f"{DAY_PATH}/day{self.day}part{self.part}.py"

    @cached_property
    def day_module_name(self):
        return f"day.day{self.day}part{self.part}"

    @cached_property
    def day_class_name(self):
        return f"Day{self.day}Part{self.part}"

    @cached_property
    def input_filename(self):
        return f"{INPUT_PATH}/{self.day}.txt"

    @cached_property
    def input(self):
        return self.read_input_file()

    def read_input_file(self):
        with open(self.input_filename) as f:
            return f.readlines()

    def run(self):
        m = import_module(self.day_module_name)
        i = getattr(m, self.day_class_name)()
        i.puzzle = self
        i.run()
