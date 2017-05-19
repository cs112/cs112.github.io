import random

class Cat(object):
    def __init__(self, weight, age, isFriendly):
        self.weight = weight
        self.age = age
        self.isFriendly = isFriendly

    def printInfo(self):
        print("I weigh", self.weight, "kg.")
        print("I am ", self.age, " years old.")
        if (self.isFriendly):
            print("I am the nicest cat in the world.")
        else:
            print("One more step and I will attack!!!")

    def feed(self, food):
        self.weight += food
        print("It was not Fancy Feast's seafood")
        self.wail()

    def wail(self):
        print("Miiiiaaaaawwwww")
        self.moodSwing()
        
    def moodSwing(self):
        self.isFriendly = (random.randint(0,1) == 0)


frisky = Cat(4.2, 2, True)
tiger = Cat(102, 5, False)

frisky.printInfo()
print()
tiger.printInfo()
print()

frisky.feed(0.2)
print()
tiger.feed(3)
print()
     
frisky.printInfo()
print()
tiger.printInfo()