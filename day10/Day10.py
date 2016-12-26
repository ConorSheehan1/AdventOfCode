class Bot:
    def __init__(self, num, value=None, instruction=""):
        self.instruction = ""
        self.num = num
        self.values = [value]

    def print(self):
        print("bot number:", self.num, self.values, self.instruction)

    def exectue(self):
        low = self.instruction[self.instruction.find("low"):self.instruction.find("and")]
        high = self.instruction[self.instruction.find("high"):]
        print(low, high)

bots = []
output = {}
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
        # skip back to top of loop
        continue

    if line.startswith("bot"):
        line = line.split(" ")
        for bot in bots:
            if bot.num == int(line[1]):
                print("old bot")
                bot.instruction = " ".join(line[2:])
                break
        else:
            print("new bot")
            bots.append(Bot(int(line[1]), int(line[1])))
        continue

# print bots in list
for bot in bots:
    bot.print()
