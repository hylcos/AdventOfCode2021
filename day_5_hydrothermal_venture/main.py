data = open("input.txt").read().splitlines()

import re
from collections import Counter

points_1 = []
points_2 = []

def cast(a,b,c,d):
    return (int(a),int(b), int(c), int(d),)

def get_range(a,b,multipler):
    if a > b:
        return [*range(a,b-1,-1)]
    if a < b:
        return [*range(a,b+1)]
    else:
        return [a] * multipler

for d in data:
    x1, y1, x2, y2 = cast(*re.search("(\d*),(\d*) -> (\d*),(\d*)", d).groups())

    diff_x = abs(x1 - x2)
    diff_y = abs(y1 - y2)
    multipler = max(diff_x, diff_y) + 1

    x_values = get_range(x1,x2, multipler)
    y_values = get_range(y1,y2, multipler)

    for x,y in zip(x_values, y_values):
        if not min(diff_x, diff_y):
            points_1.append(f"{x},{y}")
            points_2.append(f"{x},{y}")
        else:
            points_2.append(f"{x},{y}")


part_1  = len([k for k,v in Counter(points_1).items() if v > 1])
print(f"{part_1=}")

part_2  = len([k for k,v in Counter(points_2).items() if v > 1])
print(f"{part_2=}")