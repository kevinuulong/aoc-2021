from statistics import mean
from math import ceil, floor

input = *map(lambda s: int(s), open('input.txt').readline().split(',')),

def fuel(horizontal):
    fuel = 0
    for i in input:
        fuel += sum(range(1, abs(i - horizontal)+1))
    return fuel
horizontal = mean(input)
print(min(fuel(int(ceil(horizontal))), fuel(int(floor(horizontal)))))
