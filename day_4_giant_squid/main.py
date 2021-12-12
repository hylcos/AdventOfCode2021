data = open("input.txt").read().splitlines()

class BingoCard():
    card = None
    card_flipped = None

    def __init__(self, numbers) -> None:
        self.card = numbers
        self.card_flipped = list(zip(*numbers))

    def won(self, list_of_numbers):
        for c in [self.card, self.card_flipped]:
            for line in c:
                if all([n in list_of_numbers for n in line]):
                    return self.sum_of_all_unmarked_numbers(list_of_numbers)
        return -1

    def sum_of_all_unmarked_numbers(self, list_of_numbers):
        return sum([int(item) for sublist in self.card for item in sublist if item not in list_of_numbers])



if __name__ == "__main__":
    winning_numbers = data[0].split(',')
    bingo_cards_str = data[2:]
    bingo_cards = []
    for i in range(0, len(bingo_cards_str), 6):
        bingo_cards.append(BingoCard([list(filter(None,x.split(' '))) for x in bingo_cards_str[i:i+5]]))

    def part1(bingo_cards, winning_numbers):
        for i in range(0,len(winning_numbers)):
            for x in bingo_cards:
                if x.won(winning_numbers[:i]) > 0:
                    print(x.won(winning_numbers[:i]) * int(winning_numbers[i-1]))
                    return
    
    def part2(bingo_cards, winning_numbers):
        for i in range(0,len(winning_numbers)):
            x = [x.won(winning_numbers[:i]) for x in bingo_cards if x.won(winning_numbers[:i]) < 0 ]
            if len(x) == 1:
                for x in bingo_cards:
                    if x.won(winning_numbers[:i]) < 0:
                        print(x.sum_of_all_unmarked_numbers(winning_numbers[:i + 1]) * int(winning_numbers[i]))
                        return

    part1(bingo_cards, winning_numbers)
    part2(bingo_cards, winning_numbers)