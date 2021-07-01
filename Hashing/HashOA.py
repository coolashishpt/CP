# Open Addressing (Linear Probing)

class MyHash:
    def __init__(self, arrSize):
        self.arrSize = arrSize
        self.table = [-1] * arrSize 

    def hash(self, x):
        idx = x % self.arrSize
        return idx

    def insert(self, value):
        idx = self.hash(value)
        if self.table[idx] == -1:
            self.table[idx] = value
        else:
            for i in range(self.arrSize):
                n = idx + 1
                if self.table[i - n] == -1:
                    self.table[i - n] = value
                    break

        return self.table
