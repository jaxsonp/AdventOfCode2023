import math

with open("day6/input", "r") as f:
    lines = f.readlines()

# race length
t = int(lines[0].replace(" ", "").split(":")[1])

# time to beat
r = int(lines[1].replace(" ", "").split(":")[1])

"""
Equation for distance in terms of hold time (x) is:
    dist(x) = (t - x)x - r
            = -x^2 + tx - r
Below I am using the quadratic formula to calculate the distance between the roots
highschool math dub
"""
winning_holding_times = math.ceil((-t - math.sqrt(t**2 - 4 * r)) / -2) - math.floor((-t + math.sqrt(t**2 - 4 * r)) / -2 + 1)
print(f"time: {t}\ndist to beat: {r}\nnum of winning times: {winning_holding_times}")