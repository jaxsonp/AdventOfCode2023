
with open("day5/input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

initial_seeds = [int(x) for x in lines[0].split(" ")[1:]]
initial_seeds = [479518718]
print("initial seeds:", initial_seeds)

results = []
for initial_seed in initial_seeds:
    print(f"\n\nstarting with seed {initial_seed} -----------")
    val = initial_seed
    i = 0
    while i < len(lines):
        print("val:", val)
        while lines[i] != "":
            if i + 1 >= len(lines):
                break
            i += 1

        i += 2
        if i >= len(lines):
            break

        dest_start, src_start, range_len = (0, 0, 0)
        while i < len(lines) and lines[i] != "":
            dest_start, src_start, range_len = (int(x) for x in lines[i].split(" "))
            if val >= src_start and val < src_start + range_len:
                #print(f"changing val from {val} to {val + (dest_start - src_start)}")
                val += dest_start - src_start
                break
            i += 1

        #print(f"  done: {src_start} {dest_start} {range_len}. new val: {val} [offset {dest_start - src_start}]")

    results.append(val)

print("result:", results)
print("min:", min(results))