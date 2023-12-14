
with open("day5/input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

initial_seeds = []
seed_nums = [int(x) for x in lines[0].split(" ")[1:]]
for i in range(0, len(seed_nums), 2):
    initial_seeds.append((seed_nums[i], seed_nums[i + 1]))
print("initial seeds:", initial_seeds)
min_location = 0
for increment_amt in (10000, 100, 1):
    print(f"\nstepping by {increment_amt} -----------------------------")
    while True:
        val = min_location
        i = len(lines)
        while True:
            i -= 1
            if i < 0:
                break
            if lines[i] == '' or not lines[i][0].isdigit():
                continue
            dest_start, src_start, range_len = (int(x) for x in lines[i].split(" "))
            if val >= dest_start and val < dest_start + range_len:
                old_val = val
                val += src_start - dest_start

                while i > 0 and lines[i] != '' and lines[i][0].isdigit():
                    i -= 1
                i += 1

        print(f"{min_location} -> {val}", end="\r")
        valid = False
        for r in initial_seeds:
            if val >= r[0] and val < r[0] + r[1]:
                print(f"\nval found in range {r}!")
                valid = True
                break
        if valid:
            break
        min_location += increment_amt
    min_location = min_location - increment_amt
min_location += 1

print("min:", min_location)
