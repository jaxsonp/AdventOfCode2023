

with open("day1/input", "r") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    digits = [int(c) for c in line if c.isdigit()]
    sum += digits[0] * 10 + digits[-1]

print(sum)