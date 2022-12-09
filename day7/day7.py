from dataclasses import dataclass, field
from collections import namedtuple

with open("day7/input.txt") as file:
    term = file.readlines()


@dataclass
class Node:
    size: int = 0
    children: dict = None  # field(default_factory=list)


Command = namedtuple("command", ["cmd", "out"])

commands = []
for line in term:
    if line[0] == "$":
        commands.append(Command(line.lstrip("$ ").strip("\n"), []))
    else:
        commands[-1].out.append(line.strip("\n"))

commands.reverse()


def bot(cmds: list[Command], node: Node) -> None:
    while cmds:
        cmd, out = cmds.pop()
        if cmd == "cd ..":
            break

        if cmd == "ls":
            for line in out:
                sizeOrDir, name = line.split()
                if sizeOrDir.isdecimal():
                    newnode = Node(int(sizeOrDir), None)
                else:
                    newnode = Node(0, {})
                node.children[name] = newnode

        if cmd[:2] == "cd":
            name = cmd.split()[1]
            bot(cmds, node.children[name])


rootnode = Node(0, {"/": Node(0, {})})
bot(commands, rootnode)

# print(rootnode)
foldersSizes = []


def sumFolders(node: Node) -> int:
    s = 0
    for chname, ch in node.children.items():
        s += ch.size
        if type(ch.children) == dict:
            chsize = sumFolders(ch)
            s += chsize
            # print(chname, chsize)
            foldersSizes.append((chname, chsize))
    return s


sumFolders(rootnode)
print(sum(size for _, size in foldersSizes if size <= 100000))

_, totalSize = foldersSizes[-1]
toFree = 30000000 - (70000000 - totalSize)
print(min(size for _, size in foldersSizes if size >= toFree))
