with open("day1/input.txt") as file:
    food = file.read()

mostcalo = max(
    sum(int(meal) for meal in elf.split("\n") if meal != "")
    for elf in food.split("\n\n")
)
print(mostcalo)

top3 = sum(
    sorted(
        [
            sum(int(meal) for meal in elf.split("\n") if meal != "")
            for elf in food.split("\n\n")
        ],
        reverse=True,
    )[:3]
)
print(top3)
