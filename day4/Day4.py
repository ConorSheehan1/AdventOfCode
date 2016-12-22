import collections

file = open("input.txt")
count = 0
all_lines = 0


def is_real_room(ln):
    temp = ln.split("[")

    # split on -
    code = temp[0].split("-")[:-1]
    sector = temp[0].split("-")[-1]

    # remove ]
    checksum = temp[1][:-2]

    # make code single string and sort alphabetically
    code = sorted("".join(code))

    # get 5 most common values
    most_common = collections.Counter(code).most_common()
    print("most common", most_common[:5])

    m5 = ""
    while len(m5) < 5:
        # get top most common letters
        current_mc = [c for c in most_common if c[1] == most_common[0][1]]

        # sort them in alphabetical order
        letters = sorted([tup[0] for tup in current_mc])
        print("herre", current_mc, letters)

        m5 += "".join(letters)

        # remove values put into m5
        for val in current_mc:
            most_common.remove(val)

    # if most_common_5
    print(line, m5, "\n\n")
    return m5[:5] == checksum, sector


for line in file:
    val = is_real_room(line)
    if val[0]:
        count += int(val[1])

print(count, all_lines)

# 98453 too low