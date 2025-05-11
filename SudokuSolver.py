puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


columns = [[row[i] for row in puzzle] for i in range(len(puzzle[0]))]


for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        if puzzle[i][j] == 0:
            for number in range(1, 10):
                column_j = [row[j] for row in puzzle]
                if number not in puzzle[i] and number not in column_j:
                    puzzle[i][j] = number
                    break

for row in puzzle:
    print(" ".join(map(str, row)))
