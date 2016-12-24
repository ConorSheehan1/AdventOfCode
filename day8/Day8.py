def shift(row, length):
    return row[-length:] + row[:-length]


def shift_row(matrix, row, length):
    matrix[row] = shift(matrix[row], length)


# shift column in place
def shift_col(matrix, col_index, length):
    l = []
    for col in matrix:
        l.append(col[col_index])
    l = shift(l, length)
    for i in range(len(l)):
        matrix[i][col_index] = l[i]


def rect(matrix, x, y):
    # rectangle should b x wide and y tall
    for i in range(x):
        for j in range(y):
            matrix[j][i] = "#"

mat = [[1,2,3],[4,5,6],[7,8,9]]
shift_col(mat, 0, 1)
print(mat)
shift_row(mat, 0, 1)
print(mat)
rect(mat, 1, 1)
print(mat)


def handle(ln):
    if ln.startswith("rect"):
        # last char is \n so use -4 and -2, not -3, -1 for integer values in line
        print("rect", ln[-4], ln[-2])
    elif ln.startswith("rotate row"):
        ln = ln.split(" ")
        print("row", ln[-3][2:], ln[-1])
    elif ln.startswith("rotate column"):
        ln = ln.split(" ")
        print("column", ln[-3][2:], ln[-1])

file = open("input.txt")
for line in file:
    print(line[:-1])
    handle(line)
    # print(line)


