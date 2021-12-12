#   Part 1 
data = open("input.txt").read().splitlines()
max_length = max([len(d) for d in data])
gamma = ''
for i in zip(*data):
    line = ''.join(i)[::-1]
    gamma += '1' if line.count('1') > len(line) // 2 else '0'

gamma_dec = int(gamma,2)
epsilon_dec = gamma_dec ^ int('1' * max_length, 2)
epsilon = "{0:b}".format(epsilon_dec).zfill(max_length)

print(gamma_dec * epsilon_dec)

#   Part 2
def find(data, most, length=0):
    line = ''.join(list(zip(*data))[length])[::-1]
    x = '1' if line.count('1') >= len(line) / 2 else '0'

    if most:
        l = [d for d in data if d[length] == x]
    else:
        l = [d for d in data if d[length] != x]

    if len(l) == 1:
        return l[0]

    return find(l, most, length + 1)

oxygen = find(data, True)
co2 = find(data, False)
oxygen_dec = int(oxygen,2)
co2_dec = int(co2,2)

print(oxygen_dec * co2_dec)