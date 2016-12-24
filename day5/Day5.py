import hashlib
i = 0
answer = ""

while len(answer) < 8:
    md = hashlib.md5()
    # add integer to door id and encode as bytes (casting to bytes breaks for some reason)
    code = ('abbhdwsy'+str(i)).encode('utf-8')
    md.update(code)
    hash = md.hexdigest()

    # check if hex digest starts with 5 zeros and add to answer if it does
    if hash.startswith("00000"):
        answer += str(hash[5])

    i += 1

print(answer)
