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
    # most_common_5 = "".join([tup[0] for tup in collections.Counter(code).most_common(5)[:5]])
    most_common = collections.Counter(code).most_common()

    print(most_common)
    print(sorted(c[0] for c in most_common if c[1] == most_common[0][1]))

    m5 = ""
    while len(m5) < 5:
        current_mc = [c for c in most_common if c[1] == most_common[0][1]]
        letters = sorted([tup[0] for tup in current_mc])
        m5 += "".join(letters)

        # remove values put into m5
        for val in current_mc:
            most_common.remove(val)
    print(m5)
        # most_common.remove(current_mc)

    # most_dict = {}
    # for val in most_common:
    #     # hash values (get ascii value for letter, set to the power of number of occurences
    #     # most_dict[val[0]] = ord(val[0])**val[1]
    #
    #     # use z-a to inversely prioritise alphaet (z comes last)
    #     most_dict[val[0]] = (ord("z") - ord(val[0])) ** val[1]

    ## again find most common values
    # most_common_alphabetical = collections.Counter(most_dict).most_common()

    # if most_common_5
    print(line, most_common[:5], "\n", m5)




for line in file:
    val = is_real_room(line)
    # if val[0]:
    #     count += val[1]

print(count, all_lines)