import re


def decompress(some_string, num_chars, num_reps):
    return (some_string[:num_chars] * num_reps) + some_string[num_chars:]


def parse(some_string):
    i = 0
    while i < len(some_string):
        if some_string[i] == "(":
            # from i onwards get instruction (a X b), remove "(", split on x
            instruction = some_string[i:].split(")")[0][1:]

            print(instruction)

            # remove currently executing instruction from string
            some_string = re.sub(instruction, "", some_string)

            print(some_string)

            # create list of integers: convert ro integer (remove "(", slit on x
            instruction = list(map(lambda x: int(x), instruction.split("x")))

            # get chunk of text to repeat
            some_string = some_string[:i] + decompress(some_string[i:], instruction[0], instruction[1])

            print(instruction)
            print(some_string)
        i += 1


print(decompress("BC", 5, 5))
parse("(3x3)XYZ ")

file = open("input.txt")
for line in file:
    print(line.strip(" "))