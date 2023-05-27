from random import choice

class RandomizedCollection:

    def __init__(self):
        self.dict = {}
        self.values = []

    def insert(self, val: int) -> bool:
        self.values.append(val)

        isNotPresent = not val in self.dict
        if isNotPresent:
            self.dict[val] = []
        
        self.dict[val].append(len(self.values) - 1)

        return isNotPresent
        

    def remove(self, val: int) -> bool:
        if not val in self.dict:
            return False
        
        index = self.dict[val][-1]
        if index == len(self.values) - 1:
            self.values.pop()
        else:
            lastValue = self.values[-1]
            
            self.values[index] = lastValue
            
            self.dict[lastValue].pop()
            self.dict[lastValue].append(index)
            self.dict[lastValue].sort()

            self.values.pop()

        self.dict[val].pop()
        if len(self.dict[val]) == 0:
            del self.dict[val]

        return True


    def getRandom(self) -> int:
        if len(self.values) == 0:
            return -1
        
        return choice(self.values)
    
randomizedCollection = RandomizedCollection();
randomizedCollection.insert(1)                              # return true since the collection does not contain 1.
                                                            # Inserts 1 into the collection.
randomizedCollection.insert(1)                              # return false since the collection contains 1.
                                                            # Inserts another 1 into the collection. Collection now contains [1,1].
randomizedCollection.insert(2)                              # return true since the collection does not contain 2.
                                                            # Inserts 2 into the collection. Collection now contains [1,1,2].
print('random = ' + str(randomizedCollection.getRandom()))  # getRandom should:
                                                            # - return 1 with probability 2/3, or
                                                            # - return 2 with probability 1/3.
print('')

randomizedCollection.remove(1)                              # return true since the collection contains 1.
                                                            # Removes 1 from the collection. Collection now contains [1,2].
print('random = ' + str(randomizedCollection.getRandom()))  # getRandom should return 1 or 2, both equally likely.