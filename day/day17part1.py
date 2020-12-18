from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error
from enum import Enum

class Cube(Enum):
    active = "#"
    inactive = "."

class PocketDimension:
    def __init__(self, starting_cubes):
        self.cubes = starting_cubes

    @property
    def active_cube_count(self):
        return list(self.cubes.values()).count(Cube.active)

    def run_boot_cycle(self, cycles):
        new_cubes = {}
        for _ in range(cycles):
            self.expand_cubes()
            for cube_coords in self.cubes:
                new_cubes[cube_coords] = self.change_status(cube_coords)
            self.cubes = new_cubes
            
    def expand_cubes(self):
        expanded = {}
        for coords in self.cubes:
            expanded[coords] = self.cubes[coords]
            neighbors = self.neighbors(coords)
            for n in neighbors: expanded[n] = neighbors[n]
        self.cubes = expanded

    def cube(self, coords):
        return self.cubes.get(coords, Cube.inactive)

    def neighbors(self, coords):
        n = {}
        for z in range(-1,2):
            for y in range(-1,2):
                for x in range(-1,2):
                    if z == 0 and y == 0 and x == 0: continue
                    new_coords = (coords[0]+z, coords[1]+y, coords[2]+x)
                    neighbor = self.cubes.get(new_coords, Cube.inactive)
                    n[new_coords] = neighbor
        return n

    def change_status(self, coords):
        cube = self.cube(coords)
        neighbors = self.neighbors(coords)
        num_active = list(neighbors.values()).count(Cube.active)
        if cube == Cube.active:
            if num_active == 2 or num_active == 3:
                return cube
            return Cube.inactive

        if cube == Cube.inactive:
            if num_active == 3:
                return Cube.active
            return Cube.inactive

    def __str__(self):
        s = ""
        sorted_coords = sorted(self.cubes)
        current_z = sorted_coords[0][0]
        current_y = sorted_coords[0][1]
        start_y = current_y
        for coords in sorted_coords:
            if coords[0] > current_z:
                current_z = coords[0]
                current_y = start_y
                s += '\n\n'
            if coords[1] > current_y:
                current_y = coords[1]
                s += '\n'
            s += self.cubes[coords].value
        return s

class Day17Part1:
    puzzle = None

    def run(self):
        pocket_dim = PocketDimension(self.parsed_input)
        pocket_dim.run_boot_cycle(6)
        print(pocket_dim.active_cube_count)

    @cached_property
    def parsed_input(self):
        cubes = {}
        for y, col in enumerate([line.strip('\n') for line in self.puzzle.input]):
            for x, status in enumerate(list(col)):
                cubes[(0, y, x)] = Cube(status)
        return cubes
