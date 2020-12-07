from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from dataclasses import dataclass

@dataclass
class Bag:
    color: str
    quantity: int

class Day7Part1:
    puzzle = None

    def run(self):
        gold = 0
        requested_color = "shiny gold"
        self.containers = self.parsed_input
        for color in self.containers:
            if self.search_bag_for_color(color, requested_color):
                gold += 1
        print(gold)

    def search_bag_for_color(self, container_color, requested_color):
        for bag in self.containers[container_color]:
            if bag.color == requested_color: return True
            if self.search_bag_for_color(bag.color, requested_color):
                return True

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
                    bags.append(Bag(c, q))
            containers[color.strip()] = bags
        return containers
