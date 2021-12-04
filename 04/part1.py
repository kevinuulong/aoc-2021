input = open('input.txt').readlines()
input = *map(lambda s: s.replace('\n', ''), input),

nums = list(map(lambda s: int(s), input[0].split(',')))

boards,board = [],[]

for i in range(2,len(input)):
    if  i != 2 and input[i] == '' or i == len(input)-1:
        boards.append(board)
        board = []
    else:
        board.append(list(input[i].removeprefix(' ').replace('  ', ' ').split(' ')))


def check_win(boards):
    for board in boards:
        for row in board:
           if all(num[0] == 'x' for num in row):
               return board
        for column in list(zip(*board[::-1])):
            if all(num[0] == 'x' for num in column):
               return board
    return False

def check_score(board, num):
    summation = 0
    for row in board:
        summation += sum(map(lambda s: int(s), filter(lambda s: s[0] != 'x', row)))
    return summation * num

for num in nums:
    for board in boards:
        for row in board:
            for item in row:
                if item == str(num):
                    boards[boards.index(board)][board.index(row)][row.index(item)] = 'x' + item

    winner = check_win(boards)
    if winner:
        print(check_score(winner, num))
        break
