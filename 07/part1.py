from statistics import median

input = *map(lambda s: int(s), open('input.txt').readline().split(',')),
horizontal = median(input)
fuel = 0
for i in input:
    fuel += abs(i - horizontal)

print(int(fuel))
