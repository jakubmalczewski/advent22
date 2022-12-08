with open("day5/input.txt") as file:
    file = file.read()
cargo, procedure = file.split("\n\n")
print(cargo)

cargoFromTop = cargo.split("\n")
numbers = cargoFromTop[-1].split()


# build stacks
from copy import deepcopy
from collections import deque

stacks = [deque() for i in numbers]

for i, q in enumerate(stacks):
    for line in cargoFromTop[-2::-1]:
        box = line[(i) * 4 + 1]
        if box != " ":
            q.append(box)
stacksPart2 = deepcopy(stacks)

# wecan also use list instead of deque
# [[box := line[i] for line in lines[::-2] if box != " "] for i in numbers]

procedure = [
    [int(word) for word in line.split() if word.isnumeric()]
    for line in procedure.split("\n") if line != ""
]

for n,fromStack, toStack in procedure:
    for _ in range(n):
        box = stacks[fromStack - 1].pop()
        stacks[toStack - 1].append(box)

print(''.join(stack.pop() for stack in stacks))


for n,fromStack, toStack in procedure:
    carne = deque()
    for _ in range(n):
        carne.append(stacksPart2[fromStack - 1].pop())
    for _ in range(n):
        stacksPart2[toStack - 1].append(carne.pop())

print(''.join(stack.pop() for stack in stacksPart2))