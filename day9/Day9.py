import re


def decompress(some_string, num_chars, num_reps):
    return (some_string[:num_chars] * num_reps) + some_string[num_chars:]


def parse(some_string, p=True):
    i = 0
    while i < len(some_string):
        print(i)
        if some_string[i] == "(":
            # from i onwards get instruction (a X b), remove "(", split on x
            instruction = some_string[i:].split(")")[0][1:]

            # remove instruction from string
            some_string = some_string[:i] + some_string[i+len(instruction)+2:]

            if p:
                print("trim", some_string)

            # create list of integers: convert ro integer (remove "(", slit on x
            instruction = list(map(lambda x: int(x), instruction.split("x")))

            # get chunk of text to repeat (everythin up until i, then decompress section by instruction
            decompressed = decompress(some_string[i:], instruction[0], instruction[1])
            some_string = some_string[:i] + decompressed

            # i skip over length of decompressed section
            i += (instruction[0] * instruction[1])

            if p:
                print(instruction)
                print(some_string)

            # skip over increment
            continue

        i += 1
    return some_string


# # tests
# one = parse("A(1x5)BC", False)
# print(len(one))
# two = parse("(3x3)XYZ", False)
# print(len(two))
# three = parse("A(2x2)BCD(2x2)EFG", False)
# print(len(three))
# four = parse("(6x1)(1x3)A", False)
# print(len(four))
# five = parse("X(8x2)(3x3)ABCY", False)
# print(len(five))

parse("x(2x2)ab(1x4)asdf")
#
# file = open("input.txt")
# for line in file:
#     print("here", len(parse(line)))

# 128276 too high
# 123909 too high