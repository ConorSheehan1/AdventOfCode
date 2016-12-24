import collections
file = open("input.txt")

# create 9 bins (include space for new line character
collect = [[] for i in range(9)]

# add ith character of every line to ith bin in list
for line in file:
    for i in range(len(line)):
        collect[i].append(line[i])

# find most common letter for each position of all lines
answer = ""
for l in collect:
    answer += collections.Counter(l).most_common()[0][0]

print(answer)