input = open('input.txt').readlines()

increases = 0

for i in range(len(input)-2):
    increases += 1 if \
        int(input[i]) + int(input[i+1]) + int(input[i+2]) > \
        int(input[i]) + int(input[i-1]) + int(input[i+1]) else 0

print(increases)
