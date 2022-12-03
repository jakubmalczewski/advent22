with open("day3/input.txt") as file:
    backpacks = file.read()

# sanitize_input
backpacks = [b for b in backpacks.split() if b != ""]

backpacks_splited = [(b[: (half := len(b) // 2)], b[half:]) for b in backpacks]

shared = [set(c1).intersection(set(c2)).pop() for c1, c2 in backpacks_splited]


def priority(ch: str) -> int:
    a = int.from_bytes("a".encode(), "little")
    A = int.from_bytes("A".encode(), "little")
    ich = int.from_bytes(ch.encode(), "little")
    return (ich - a + 1) if ch.islower() else (ich - A + 27)


print(sum(priority(item) for item in shared))

n_elfs = len(backpacks)
assert n_elfs % 3 == 0

groups = [backpacks[i : i + 3] for i in range(0, n_elfs, 3)]
badges = [
    set(e1).intersection(set(e2)).intersection(set(e3)).pop() for e1, e2, e3 in groups
]
print(sum(priority(item) for item in badges))
