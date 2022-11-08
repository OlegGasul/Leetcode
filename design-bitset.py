class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bitSet = [0] * size
        self.interpretation = True
        self.onesCount = 0

    def fix(self, idx: int) -> None:
        if self.interpretation:
            if self.bitSet[idx] == 0:
                self.bitSet[idx] = 1
                self.onesCount += 1
        else:
            if self.bitSet[idx] == 1:
                self.bitSet[idx] = 0
                self.onesCount += 1

    def unfix(self, idx: int) -> None:
        if self.interpretation:
            if self.bitSet[idx] == 1:
                self.bitSet[idx] = 0
                self.onesCount -= 1
        else:
            if self.bitSet[idx] == 0:
                self.bitSet[idx] = 1
                self.onesCount -= 1

    def flip(self) -> None:
        self.onesCount = self.size - self.onesCount
        self.interpretation = not self.interpretation

    def all(self) -> bool:
        return self.onesCount == self.size

    def one(self) -> bool:
        return self.onesCount > 0

    def count(self) -> int:
        return self.onesCount
        
    def toString(self) -> str:
        result = ""
        
        for bit in self.bitSet:
            if self.interpretation:
                result += "1" if bit == 1 else "0"
            else:
                result += "0" if bit == 1 else "1"

        return result

bitSet = Bitset(5)
bitSet.fix(3)
bitSet.fix(1)
bitSet.flip()
print(bitSet.all())
bitSet.unfix(0)
bitSet.flip()
print(bitSet.one())
bitSet.unfix(0)
print(bitSet.count())
print(bitSet.toString())