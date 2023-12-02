nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("day1/input", "r") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    digits = []
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(int(line[i]))
        else:
            for j, num_str in zip(range(1, 10), nums):
                if line[i:i+len(num_str)] == num_str:
                    digits.append(j)

    sum += digits[0]*10 + digits[-1]


print(sum)