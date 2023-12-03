
with open("day3/input", "r") as f:
    input = f.read()

def is_symbol (c: chr):
    return c != '.' and c != '\n' and not c.isdigit()

i = 0
star_num_count = [0] * len(input)
star_nums = [1] * len(input)
line_length = len(input.split("\n")[0]) + 1
print("line length:", line_length)
while i < len(input):
    # print(i, input[i])
    if input[i].isdigit():
        num_length = 0
        d = input[i]
        # finding num length
        while d.isdigit():
            num_length += 1
            d = input[i + num_length]
        # print(input[i:i + num_length])
        num = int(input[i:i + num_length])

        is_part = False
        if i - 1 >= 0 and input[i - 1] == '*':
            star_nums[i - 1] *= num
            star_num_count[i - 1] += 1
            print(f"star num {num} at {i - 1}")
        elif i + num_length < len(input) and input[i + num_length] == '*':
            print(f"star num {num} at {i + num_length}")
            star_nums[i + num_length] *= num
            star_num_count[i + num_length] += 1
        else:
            for j in range(-1, num_length + 1):
                if (i - line_length) + j >= 0 and input[(i - line_length) + j] == '*':
                    star_nums[(i - line_length) + j] *= num
                    star_num_count[(i - line_length) + j] += 1
                    print(f"star num {num} at {(i - line_length) + j}")
                    break
                if i + line_length + j < len(input) and input[i + line_length + j] == '*':
                    star_nums[i + line_length + j] *= num
                    star_num_count[(i + line_length) + j] += 1
                    print(f"star num {num} at {(i + line_length) + j}")
                    break

        i += num_length
    else:
        i += 1

sum = 0
print(star_nums)
for i in range(len(star_num_count)):
    if star_num_count[i] == 2:
        # print(f"gear nums: {star_nums[i][0]} * {star_nums[i][1]}")
        sum += star_nums[i]

print("sum:", sum)