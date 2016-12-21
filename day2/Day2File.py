grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# top row is 0, bottom row is 2


def getNumber(user_string, x=1, y=1):
    for cmd in user_string:

        # as long as you're not at the top row, move up one row
        if cmd == "U" and y > 0:
            y -= 1

        # as long as you're not at the bottom row, move down one row
        elif cmd == "D" and y < 2:
            y += 1

        # more intuitive list indexing for left and right
        elif cmd == "R" and x < 2:
            x += 1

        # use elif just in case invalid input is used
        elif cmd == "L" and x > 0:
            x -= 1

    print(grid[y][x])
    return x, y


file = open("day2_input.txt")
# for line in file:
#     print(line)

counter = 0
for line in file:
    # print(line)
    if counter == 0:
        previous_position = getNumber(line)
    if counter > 0:
        current_position = getNumber(line, previous_position[0], previous_position[1])
        previous_position = current_position
    counter += 1


# test, should be 1985
# ULL
# RRDDD
# LURDL
# UUUUD
