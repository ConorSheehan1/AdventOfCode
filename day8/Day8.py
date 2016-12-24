def shift_row(row, length):
    return row[-length:] + row[:-length]

# shift column in place
def shift_col(matrix, col_index, length):
    l = []
    for col in matrix:
        l.append(col[col_index])
    l = shift_row(l, length)
    for i in range(len(l)):
        matrix[i][col_index] = l[i]




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



#
# file = open("input.txt")
# for line in file:
#     print(line[:-1])
#     handle(line)
#     # print(line)

print(shift_row([1,2,3,4,5], 5))

