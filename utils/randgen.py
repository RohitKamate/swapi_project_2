import random


class ProduceChars:
    """generator class to produce random numbers in a given range"""
    def __init__(self, start: int, stop: int, range1: int):
        self.start = start
        self.stop = stop
        self.range1 = range1

    def randrange(self):
        ranges = (random.randrange(self.start, self.stop) for _ in range(self.start, self.range1+1))
        return list(ranges)


if __name__ == "__main__":
    a = ProduceChars(0, 3, 2)
    print(a.randrange())
