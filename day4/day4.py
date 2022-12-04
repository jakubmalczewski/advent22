from collections.abc import Iterable

with open("day4/input.txt") as file:
    pairs = file.read()
pairs = [p for p in pairs.split("\n") if p != ""]

pairs = [
    [[int(r) for r in strrange.split("-")] for strrange in p.split(",")] for p in pairs
]


def f1(pair: Iterable[Iterable[int]]) -> bool:
    x1, x2 = pair
    x1min, x1max = x1
    x2min, x2max = x2
    if x1min >= x2min and x1max <= x2max:
        return True
    if x1min <= x2min and x1max >= x2max:
        return True
    return False


print(sum(f1(p) for p in pairs))
sets = [
    (set(range(lim1[0], lim1[1] + 1)), set(range(lim2[0], lim2[1] + 1)))
    for lim1, lim2 in pairs
]
print(sum(1 for set1, set2 in sets if set1.issubset(set2) or set1.issuperset(set2)))

def f2(pair: Iterable[Iterable[int]]) -> bool:
    x1, x2 = pair
    x1min, x1max = x1
    x2min, x2max = x2
    if x1max >= x2min and x1min <= x2max:
        return True
    if x2max >= x1min and x2min <= x1max:
        return True
    return False


print(sum(f2(p) for p in pairs))
print(sum(1 for set1, set2 in sets if len(set1.intersection(set2)) > 0 ))
