import re

#   Part 1
class Submarine():
    horizontal_position = 0
    depth = 0

    def up(self, amount: int) -> None:
        self.depth -= amount

    def down(self, amount: int) -> None:
        self.depth += amount

    def forward(self, amount: int) -> None:
        self.horizontal_position += amount

    @property
    def current_location(self) -> int:
        return self.horizontal_position * self.depth

#   Part 2
class Submarine2():
    horizontal_position = 0
    aim = 0
    depth = 0

    def up(self, amount: int) -> None:
        self.aim -= amount

    def down(self, amount: int) -> None:
        self.aim += amount

    def forward(self, amount: int) -> None:
        self.depth += amount * self.aim
        self.horizontal_position += amount

    @property
    def current_location(self) -> int:
        return self.horizontal_position * self.depth


if __name__ == "__main__":
    lines = open("input.txt").read().splitlines()
    s = Submarine()
    s2 = Submarine2()
    for line in lines:
        f, a = re.match(r'(.*?)\s(\d*)', line).groups()
        getattr(s,f)(int(a))
        getattr(s2,f)(int(a))
    print(s.current_location)
    print(s2.current_location)