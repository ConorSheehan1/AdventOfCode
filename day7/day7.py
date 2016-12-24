def supports_tls(ip):
    # using sliding window 4 characters wide
    ans = []
    for i in range(len(ip)-3):
        # if the first two letters are the reverse of the last tow letters,
        # and the first letter is different to the second
        ans.append(ip[i:i+2] == ip[i+2:i+4][::-1] and ip[i] != ip[i+1])

    # if any of the strings in the sliding window were true return true
    return any(ans)

count = 0
file = open("input.txt")

for line in file:
    # split lines into square bracket chunks
    ip = line.split("[")
    ip = list(map(lambda x: x.split("]"), ip))

    # flatten nested list
    ip = [item for sublist in ip for item in sublist]

    # initialise flag to false, change to true if ip could support tls, switch to flase and break if it can't
    flag = False

    # if support tls for any odd chunk is true and support tls for all even chunks is false, ip supports tls
    for i in range(len(ip)):
        if i % 2 == 0 and supports_tls(ip[i]):
            flag = True
        # if ip has any 4 letter palindrome within quare brackets, ip doesn't support tls so break
        if i % 2 == 1 and supports_tls(ip[i]):
            flag = False
            break

    if flag:
        count += 1

print(count)

# 208 too high
# 108 too low