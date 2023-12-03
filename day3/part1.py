
with open("day3/input", "r") as f:
    input = f.read()

def is_symbol (c: chr):
    return c != '.' and c != '\n' and not c.isdigit()

i = 0
part_nums = []
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
        print(input[i:i + num_length], end="")

        is_part = False
        if i - 1 >= 0 and is_symbol(input[i - 1]):
            is_part = True
            print("\tsymbol left")
        elif i + num_length < len(input) and is_symbol(input[i + num_length]):
            is_part = True
            print("\tsymbol right")
        else:
            for j in range(-1, num_length + 1):
                if (i - line_length) + j >= 0 and is_symbol(input[(i - line_length) + j]):
                    is_part = True
                    print("\tsymbol above")
                    break
                if i + line_length + j < len(input) and is_symbol(input[i + line_length + j]):
                    is_part = True
                    print("\tsymbol below")
                    break
        if is_part:
            part_nums.append(int(input[i:i+num_length]))
        else:
            print("\tno symbol found :(")

        i += num_length
    else:
        i += 1

print(part_nums)
print("sum:", sum(part_nums))

