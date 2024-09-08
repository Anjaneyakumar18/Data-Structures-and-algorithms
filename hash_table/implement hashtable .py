class HashTable:

    def __init__(self):
        self.table = []
        self.keys = []

    def insert(self, key, value)->None:
        self.keys.append(key)
        self.table.append([key, value])
        return

    def update(self, key, val)->None:
        if key in self.keys:
            for i in range(len(self.table)):
                if self.table[i][0] == key:
                    self.table[i][1] = val
                    return
        else:
            print("key doesn't exist")

    def delete(self, key)->None:
        if key not in self.keys:
            return print("no key found")
        for i in range(len(self.table)):
            if self.table[i][0] == key:
                self.table.pop(i)
                break
    def view(self)->None:
        for i in range(len(self.table)):
            print(self.table[i][0],'->',self.table[i][1])


# Example usage
HT = HashTable()
HT.insert(1, 10)
HT.insert(2, 20)
HT.insert(3, 30)
HT.view()
HT.update(3,300)
HT.view()
HT.delete(1)
HT.view()