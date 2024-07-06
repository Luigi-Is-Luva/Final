class vector:
    def __init__(self, arr):
        self.arr = arr

    def getArr(self):
        return self.arr

    def setArr(self, arr):
        self.arr = arr

    def popBack(self):
        if self.arr:
            self.arr.pop()

    def pushBack(self, x):
        self.arr.append(x)

    def get(self, n):
        if 0 <= n < len(self.arr):
            return self.arr[n]
        else:
            return None
# Test Cases

my_vect = vector([10, 20, 30])
print(my_vect.arr) # Working init up to here

print(my_vect.getArr()) # Working getter function

my_vect.setArr([33, 66, 99]) # Working setter function

my_vect.popBack()
my_vect.popBack()

print(my_vect.getArr()) # If this prints out 33, then working pop function

my_vect.pushBack(333)
my_vect.pushBack(3333)

print(my_vect.getArr()) # If this prints 33, 333, 3333, then push is working

print(my_vect.get(1)) # If this prints 333, then get is working