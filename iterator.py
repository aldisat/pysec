# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
# print(next(myit))

#==========================
# class Mynumbers:
    # def __iter__(self):
        # self.a = 1
        # return self
    # def __next__(self):
        # x = self.a
        # self.a += 1
        # return x

# myclass = Mynumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


#=========================

class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = Mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

        

