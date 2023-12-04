
with open("day4/input", "r") as f:
    lines = f.readlines()

card_count = [1] * len(lines)
for i, line in zip(range(len(lines)), lines):
    points = 0
    winning_nums = [int(n) for n in line.split(": ")[1].split(" | ")[0].split(" ") if n != '']
    matching_nums = 0
    for num in [int(n) for n in line.split(" | ")[1].split(" ") if n != '']:
        if num in winning_nums:
            matching_nums += 1
            if points == 0:
                points = 1
            else:
                points *= 2
    print(f"card {i} had {matching_nums} matches")
    for j in range(1, matching_nums + 1):
        card_count[i + j] += card_count[i]

print(card_count)
print("sum:", sum(card_count))