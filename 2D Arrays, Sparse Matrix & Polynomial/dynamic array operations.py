class DynamicArray:
    def __init__(self):
        self.arr = []

    def insert_end(self, value):
        self.arr.append(value)

    def insert_at(self, index, value):
        self.arr.insert(index, value)

    def delete_at(self, index):
        if 0 <= index < len(self.arr):
            self.arr.pop(index)

    def search(self, value):
        return self.arr.index(value) if value in self.arr else -1

    def display(self):
        print(self.arr)

da = DynamicArray()
da.insert_end(10)
da.insert_end(20)
da.insert_at(1, 15)
da.display()         # [10, 15, 20]
da.delete_at(0)
da.display()         # [15, 20]
print(da.search(20)) # 1
print(da.search(99)) # -1
