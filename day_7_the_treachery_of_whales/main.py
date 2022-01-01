data = sorted([int(x) for x in open("input.txt").read().split(',')])

def calc_fuel_1(d, target):
    return sum([abs(target - x) for x in d])


def calc_fuel_2(d, target):
    return sum([(sum(range(1,abs(target - x)+1))) for x in d])

found = False
diff = 1
avd = sum(data) // len(data)
while not found:
    print(f"{diff=}")
    avg = [calc_fuel_2(data, x) for x  in range(avd-1, avd + 2)]
    if avg[0] < avg[1]:
        avd += avd / 2 
    elif avg[2] < avg[1]:
        avd -= avd / 2 
    else:
        found = True
        print(f"anwser: {avg[2]}")
        
