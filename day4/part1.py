
with open("day4/input", "r") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    points = 0
    winning_nums = [int(n) for n in line.split(": ")[1].split(" | ")[0].split(" ") if n != '']
    for num in [int(n) for n in line.split(" | ")[1].split(" ") if n != '']:
        found = False
        if num in winning_nums:
            if points == 0:
                points = 1
            else:
                points *= 2
    sum += points

print(sum)