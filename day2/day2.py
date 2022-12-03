from enum import Enum

with open("day2/input.txt") as file:
    moves = file.read()

moves = [move.split(" ") for move in moves.split("\n")]


class Move(Enum):
    A = 0
    B = 1
    C = 2
    X = 0
    Y = 1
    Z = 2


score_table = ((3, 6, 0), 
               (0, 3, 6), 
               (6, 0, 3))


def fight(elf: str, me: str) -> int:
    return score_table[Move[elf].value][Move[me].value]


def score(elf: str, me: str) -> int:
    return fight(elf, me) + (Move[me].value + 1)


print(sum(score(e, m) for e, m in moves))

def what2play(elf:str, result:str) -> tuple[str, str]:
    match result:
        case "Y":
            return elf, elf
        case "X":
            return elf, ("A","B","C")[(Move[elf].value + 2) % 3]
        case "Z":
            return elf, ("A","B","C")[(Move[elf].value + 1) % 3]

print(sum(score(*what2play(e, t)) for e, t in moves))