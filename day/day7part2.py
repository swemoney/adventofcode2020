from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from dataclasses import dataclass
import math

@dataclass
class Bag:
    color: str
    quantity: int

class Day7Part2:
    puzzle = None

    def run(self):
        requested_color = "shiny gold"
        self.containers = self.parsed_input
        
        n = 0
        n = self.find_number_of_bags_inside(requested_color)
        print(n)

    def find_number_of_bags_inside(self, color):
        current_count = 0
        for bag in self.containers[color]:
            current_count += bag.quantity + (self.find_number_of_bags_inside(bag.color) * bag.quantity)
        return current_count

    @cached_property
    def parsed_input(self):
        containers = {}
        for rule in self.puzzle.input:
            bags = []
            color = rule.split("bags contain ")[0]
            bags_contained = rule.split("bags contain ")[1].replace('\n',"")
            if bags_contained != "no other bags.":
                for bag_string in bags_contained.split(", "):
                    q = bag_string.split(" ")[0]
                    c = " ".join(bag_string.split(" ")[1:3])
                    bags.append(Bag(c, int(q)))
            containers[color.strip()] = bags
        return containers
