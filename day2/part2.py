
with open("day2/input", "r") as f:
    lines = f.read().strip()

sum = 0
for line in lines.split("\n"):
    index = int(line.split(": ")[0][5:])
    line = line.split(": ")[1]

    sets = line.split("; ")
    min_r, min_g, min_b = (0, 0, 0)
    for set in sets:
        tokens = set.replace(",", "").split(" ")
        for i in range(len(tokens)):
            if tokens[i] == "red":
                min_r = max(min_r, int(tokens[i-1]))
            elif tokens[i] == "green":
                min_g = max(min_g, int(tokens[i-1]))
            elif tokens[i] == "blue":
                min_b = max(min_b, int(tokens[i-1]))
    sum += min_r * min_g * min_b


print("sum:", sum)