input = open('input.txt').readlines()
input = map(lambda s: s.replace('\n', ''), input)

depth = 0
horizontal = 0

for string in input:
    replaced = string.replace('down ', '') if 'down' in string else string.replace('up ', '-')
    if replaced != string:
        depth += int(replaced)
    else:
        horizontal += int(string.replace('forward ',''))

print(depth*horizontal)