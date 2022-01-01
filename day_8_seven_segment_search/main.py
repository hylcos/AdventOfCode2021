data = open("input.txt").read().splitlines()
all_answers = []

def numbers_of_length(signal, length):
    return [x for x in signal if len(x) == length]

def contain_all_letters(part1, part2):
    for x in part1:
        if x not in part2:
            return False
    return True

def get_and_pop(signal, length):
    x = numbers_of_length(signal, length)[0]
    signal.remove(x)
    return x

def sort_str(x):
    return ''.join(sorted(x))

for line in data:
    signal_pattern, output = line.split("|")
    signal_pattern = signal_pattern.split()

    one = get_and_pop(signal_pattern, 2)
    seven = get_and_pop(signal_pattern, 3)
    four = get_and_pop(signal_pattern, 4)


    nine = [s for s in numbers_of_length(signal_pattern, 6) if contain_all_letters(four, s)][0]
    signal_pattern.remove(nine)
    
    zero = [s for s in numbers_of_length(signal_pattern, 6) if contain_all_letters(one, s)][0]
    signal_pattern.remove(zero)

    three = [s for s in numbers_of_length(signal_pattern, 5) if  contain_all_letters(one, s)][0]
    signal_pattern.remove(three)

    six = get_and_pop(signal_pattern, 6)

    five = [s for s in numbers_of_length(signal_pattern, 5) if contain_all_letters(s, nine)][0]
    signal_pattern.remove(five)

    two = get_and_pop(signal_pattern, 5)

    numbers = {
        sort_str(zero): 0, 
        sort_str(one): 1, 
        sort_str(two): 2, 
        sort_str(three): 3, 
        sort_str(four): 4,
        sort_str(five): 5, 
        sort_str(six): 6, 
        sort_str(seven): 7, 
        sort_str(signal_pattern.pop()): 8, 
        sort_str(nine): 9
    }

    number_generated = ''
    for x in output.split():
        number_generated += str(numbers[''.join(sorted(x))])
    
    all_answers.append(int(number_generated))

print(f"{sum(all_answers)=}")
        
