input = open('input.txt').readlines()

increases = 0

for i in range(1,len(input)):
    increases += 1 if int(input[i]) > int(input[i-1]) else 0

print(increases)
