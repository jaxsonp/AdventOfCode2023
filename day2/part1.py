
with open("day2/input", "r") as f:
    lines = f.read().strip()

sum = 0
for line in lines.split("\n"):
    index = int(line.split(": ")[0][5:])
    line = line.split(": ")[1]

    sets = line.split("; ")
    invalid = False
    for set in sets:
        tokens = set.replace(",", "").split(" ")
        for i in range(len(tokens)):
            if (tokens[i] == "red" and int(tokens[i-1]) > 12) or (tokens[i] == "green" and int(tokens[i-1]) > 13) or (tokens[i] == "blue" and int(tokens[i-1]) > 14):
                invalid = True
                break
        if invalid:
            break

    if not invalid:
        print(index)
        sum += index

print("sum:", sum)