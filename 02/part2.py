input = open('input.txt').readlines()
input = map(lambda s: s.replace('\n', ''), input)

depth = 0
horizontal = 0
aim = 0

for string in input:
    replaced = string.replace('down ', '') if 'down' in string else string.replace('up ', '-')
    if replaced != string:
        aim += int(replaced)
    else:
        x = int(string.replace('forward ',''))
        horizontal += x
        depth += x * aim

print(depth*horizontal)