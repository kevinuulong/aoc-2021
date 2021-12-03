from statistics import mode

input = open('input.txt').readlines()
input = *map(lambda s: s.replace('\n', ''), input),

gamma = ''

for i in range(len(input[0])):
    gamma += mode(map(lambda s: s[i], input))

gamma = int(gamma, 2)
epsilon = gamma ^ int('1'*(len(input[0])), 2)

print(gamma * epsilon)