with open("day6/input.txt") as file:
    mess = file.read()

for i in range(len(mess)):
    if len(set(mess[i:i+4])) == 4:
        print(i + 4)
        break


for i in range(len(mess)):
    if len(set(mess[i:i+14])) == 14:
        print(i + 14)
        break