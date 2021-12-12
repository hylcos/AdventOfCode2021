#   Part 1
data = open("input.txt").read().splitlines()
dec = len([x for x in range(len(data[:-1])) if data[x + 1] > data[x]])
print(f"{dec=}")

#   Part 2 
data = [sum(data[x:x+3]) for x in range(len(data[:-2]))]
dec = len([x for x in range(len(data[:-1])) if data[x + 1] > data[x]])
print(f"{dec=}")