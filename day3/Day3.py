file = open("input.txt")
count = 0
all_lines = 0


def is_triangle(nums):
    counter = 0
    for i in range(len(nums)):
        # circularly index list, if every side is less than the sum of remaining sides
        if (nums[(i+1) % len(nums)] + nums[(i+2) % len(nums)]) > nums[i]:
            counter += 1
    return counter == 3


for line in file:
    # remove "\n from string using slice, split on space, removed empty string
    nstrings = filter(lambda s: s != "", line[:-1].split(" "))
    # cast all string to int
    numbers = list(map(lambda n: int(n), nstrings))

    # if values are valid triangle, increment count
    if is_triangle(numbers):
        count += 1

    all_lines += 1

print(count)
# 817 too low

