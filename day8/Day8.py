class Screen:
    def __init__(self, width, height):
        self.screen = []
        for col in range(height):
            self.screen.append(["."]*width)

        # self.screen = [["."]*width]*height

    def shift(self, row, length):
        return row[-length:] + row[:-length]

    def shift_row(self, row, length):
        self.screen[row] = self.shift(self.screen[row], length)

    # shift column in place
    def shift_col(self, col_index, length):
        l = []
        for col in self.screen:
            l.append(col[col_index])
        l = self.shift(l, length)
        for i in range(len(l)):
            self.screen[i][col_index] = l[i]

    def rect(self, x, y):
        # rectangle should b x wide and y tall
        for i in range(x):
            for j in range(y):
                self.screen[j][i] = "#"

    def handle(self, ln):
        if ln.startswith("rect"):
            # split on x to get height rectangle should be
            ln = ln.split("x")
            # split left value on space to get width rectangle should be
            print("rect", int(ln[0].split(" ")[-1]), int(ln[1]))
            self.rect(int(ln[0].split(" ")[-1]), int(ln[1]))
            self.print_screen()

        elif ln.startswith("rotate row"):
            ln = ln.split(" ")
            # go from 2 on to remove "x=", choose -3 to skip "by"
            print("row", int(ln[-3][2:]), int(ln[-1]))
            self.shift_row(int(ln[-3][2:]), int(ln[-1]))
            self.print_screen()

        elif ln.startswith("rotate column"):
            ln = ln.split(" ")
            print("col", int(ln[-3][2:]), int(ln[-1]))
            self.shift_col(int(ln[-3][2:]), int(ln[-1]))
            self.print_screen()

    def print_screen(self):
        for col in self.screen:
            print(col)

    def pixel_count(self):
        count = 0
        for col in self.screen:
            count += col.count("#")
        return count


s = Screen(50, 6)
# s = Screen(5, 5)
s.print_screen()

file = open("input.txt")
for line in file:
    print(line[:-1])
    s.handle(line)

s.print_screen()
print(s.pixel_count())

# 47 too low
