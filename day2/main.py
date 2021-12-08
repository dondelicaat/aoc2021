import os


class Submarine:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def down(self, amount):
        self.aim += amount

    def up(self, amount):
        self.aim -= amount

    def forward(self, amount):
        self.y += (self.aim * amount)
        self.x += amount

    def run(self):
        with open(f"{os.getcwd()}/day2/input.txt", "r") as f:
            for line in f.readlines():
                op, amount = line.split(" ")
                operation = getattr(self, op)
                operation(int(amount))

                print(self.x, self.y, self.aim)


sub = Submarine()
sub.run()
print(sub.x * sub.y)

