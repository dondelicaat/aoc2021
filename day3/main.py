import os


class Submarine:
    def __init__(self):
        self.numbers = list()
        self.num_bits = 0

    def get_oxygen_rating(self):
        for idx in range(self.num_bits):
            if len(self.numbers) == 1:
                return int(self.numbers[0], 2)
            count = self.get_counter()[idx]
            bit_to_keep = 0 if count < 0 else 1
            self.filter(idx, bit_to_keep)

        if len(self.numbers) != 1:
            raise ValueError("Should only be one value.")
        else:
            return int(self.numbers[0], 2)

    def get_co2_rating(self):
        for idx in range(self.num_bits):
            if len(self.numbers) == 1:
                return int(self.numbers[0], 2)
            count = self.get_counter()[idx]
            if count == 0:
                bit_to_keep = 0
            elif count > 0:
                bit_to_keep = 0
            else:
                bit_to_keep = 1
            self.filter(idx, bit_to_keep)

        if len(self.numbers) != 1:
            raise ValueError("Should only be one value.")
        else:
            return int(self.numbers[0], 2)

    def filter(self, index, bit):
        self.numbers = [number for number in self.numbers if number[index] == str(bit)]

    def get_counter(self):
        bitcounter = [0] * self.num_bits
        for number in self.numbers:
            for index, val in enumerate(number):
                bitval = int(number[index])
                bitcounter[index] += -1 if bitval == 0 else 1

        return bitcounter

    def run(self):
        with open(f"{os.getcwd()}/day3/input.txt", "r") as f:
            for line in f.readlines():
                self.num_bits = len(line.strip())
                self.numbers.append(line.strip())




sub = Submarine()
sub.run()
sub.gamma()
ox = sub.get_oxygen_rating()
sub12 = Submarine()
sub12.run()
co2 = sub12.get_co2_rating()

print(co2,ox, co2*ox)

