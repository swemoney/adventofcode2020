from functools import cached_property
from puzzle import Puzzle # pylint: disable=import-error

# [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4] -> [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
#
# Start with a dict (d) and loop through each sorted adapter...
# d = {0: 1}
# 1:  [1-1=0, 1-2=-1, 1-3=-2]
#     [d[0]=1, d[-1]=0, d[-2]=0] = 1
#     >> d[1] = 1
# 4:  [4-1=3, 4-2=2, 4-3=1]
#     [d[0]=0, d[2]=0, d[1]=1] = 1
#     >> d[4] = 1
# 5:  [5-1=4, 5-2=3, 5-3=2]
#     [d[4]=1, d[3]=0, d[2]=0] = 1
#     >> d[5] = 1
# 6:  [6-1=5, 6-2=4, 6-3=3]
#     [d[5]=1, d[4]=1, d[3]=0] = 2
#     >> d[6] = 2
# 7:  [7-1=6, 7-2=5, 7-3=4]
#     [d[6]=2, d[5]=1, d[4]=1] = 4
#     >> d[7] = 4
# 10: [10-1=9, 10-2=8, 10-3=7]
#     [d[9]=0, d[8]=0, d[7]=4] = 4
#     >> d[10] = 4
# 11: [11-1=10, 11-2=9, 11-3=8]
#     [d[10]=4, d[9]=0, d[8]=0] = 4
#     >> d[11] = 4
# 12: [12-1=11, 12-2=10, 12-3=9]
#     [d[11]=4, d[10]=4, d[9]=0] = 8
#     >> d[12] = 8
# 15: [15-1=14, 15-2=13, 15-3=12]
#     [d[14]=0, d[13]=0, d[12]=8] = 8
#     >> d[15] = 8
# 16: [16-1=15, 16-2=14, 16-3=13]
#     [d[15]=8, d[14]=0, d[13]=0] = 8
#     >> d[16] = 8
# 19: [19-1=18, 19-2=17, 19-3=16]
#     [d[18]=0, d[17]=0, d[16]=8] = 8
#     >> d[19] = 8
# 22: [22-1=21, 22-2=20, 22-3=19]
#     [d[21]=0, d[20]=0, d[19]=8] = 8
#     >> d[22] = >> 8 <<

class Day10Part2:
    puzzle = None

    def run(self):
        adapters = self.parsed_input
        paths = self.find_valid_arrangements(adapters)
        print(paths)

    def find_valid_arrangements(self, adapters):
        checked_adapters = {0: 1}
        for adapter in adapters:
            # Check adapter differences of 1-3 in checked adapters (0 if it doesn't exist)
            diffs = [checked_adapters.get(adapter-d,0) for d in range(1,4)]
            checked_adapters[adapter] = sum(diffs) # Add up all the differences we found
        return checked_adapters[adapters[-1]] # Our device joltage key should have the total number of paths found

    @cached_property
    def parsed_input(self):
        adapters = [int(line.strip('\n')) for line in self.puzzle.input]
        return sorted(adapters + [max(adapters) + 3])
