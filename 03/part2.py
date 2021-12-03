input = open('input.txt').readlines()
input = *map(lambda s: s.replace('\n', ''), input),

def rating(list, o):
    for i in range(len(list[0])):
        zeroes = []
        ones = []
        if (len(list)>1):
            for s in list:
                zeroes.append(s) if s[i] == '0' else ones.append(s)
            if o:
                list = zeroes if len(zeroes) > len(ones) else ones
            else:
                list = ones if len(ones) < len(zeroes) else zeroes
    return int(list[0], 2)

print(rating(input, True) * rating(input, False))