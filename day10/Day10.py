class Bot:
    def __init__(self, num, value):
        self.instruction = ""
        self.values = [value]
        self.num = num

    def print(self):
        print("bot number:", self.num, self.values, self.instruction)

bots = []
file = open("test.txt")
for line in file:
    if line.startswith("value"):
        print(line, end="")
        line = line.split(" ")

        # check if bot already exists, if it does, append value, otherwise make new bot
        for bot in bots:
            if bot.num == int(line[-1]):
                print("old bot")
                bot.values.append(int(line[1]))
                break
        else:
            print("new bot")
            bots.append(Bot(int(line[-1]), int(line[1])))

        # print bots in list
        for bot in bots:
            bot.print()
        print()



    # " ".join(line[:-1])