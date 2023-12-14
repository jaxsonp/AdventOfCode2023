import math

with open("day6/input", "r") as f:
    lines = f.readlines()
times = [int(x) for x in lines[0].split(" ")[1:] if x != ""]
distances = [int(x) for x in lines[1].split(" ")[1:] if x != ""]

product = 1
for i, t, r in zip(range(len(times)), times, distances):
    """
        t == race length
        r == record distance

    Equation for distance in terms of hold time (x) is:
        dist(x) = (t - x)x - r
                = -x^2 + tx - r
    Below I am using the quadratic formula to calculate the distance between the roots
    highschool math dub
    """
    winning_holding_times = math.ceil((-t - math.sqrt(t**2 - 4 * r)) / -2) - math.floor((-t + math.sqrt(t**2 - 4 * r)) / -2 + 1)
    print(f"race {i}\n - time: {t}\n - dist to beat: {r}\n - num of winning times: {winning_holding_times}")
    product *= winning_holding_times

print("output:", product)