user = input().split(", ")
# north, south, east, west
distance = {"north": 0, "south": 0, "east": 0, "west": 0}

# orientation (circular list)
orient = ["north", "east", "south", "west"]


# start facing north (oriented north)
current = 0

# for every direction command
for val in user:
    # find orientation
    if val[0] == "L":
        current = (current-1) % len(orient)
    else:
        current = (current+1) % len(orient)

    # orient converts current direction into key for distance
    distance[orient[current]] += int(val[1:])


def getDistance(dist):
    # distance as [0, 0] coordinate is north-south, east-west
    # get absolute value and sum to get total number of blocks away
    return abs(dist["north"]-dist["south"]) + abs(dist["east"]-dist["west"])



print(distance)
print(getDistance(distance))

# L1, L1, L1
# L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2
