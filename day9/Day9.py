import re


def decompress(some_string, num_chars, num_reps):
    return (some_string[:num_chars] * num_reps) + some_string[num_chars:]


def parse(some_string):
    i = 0
    while i < len(some_string):
        print(i, len(some_string))
        if some_string[i] == "(":
            # from i onwards get instruction (a X b), remove "(", split on x
            instruction = some_string[i:].split(")")[0][1:]

            # remove instruction from string
            some_string = some_string[:i] + some_string[i+len(instruction)+2:]
            print("trim", some_string)

            # create list of integers: convert ro integer (remove "(", slit on x
            instruction = list(map(lambda x: int(x), instruction.split("x")))

            # get chunk of text to repeat (everythin up until i, then decompress section by instruction
            decompressed = decompress(some_string[i:], instruction[0], instruction[1])
            some_string = some_string[:i] + decompressed

            # i skip over length of decompressed section
            i += (instruction[0] * instruction[1])
            print(i)

            print(instruction)
            print(some_string)

        i += 1


# print(decompress("BC", 5, 5))
parse("(4x2)XYZ(1x2)abc")

# file = open("input.txt")
# for line in file:
#     print(line.strip(" "))