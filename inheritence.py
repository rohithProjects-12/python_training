class Person():
    CityName = "mumbai"
    def printName(self,name):
        print(name)

class Ashok(Person):
    def printDetails(self):
        print("some message")

class Arun(Person):
    def printDetails(self):
        print("some message")


obj  = Ashok()
obj.CityName = "new city"
obj.printName("ashok")

obj1 = Arun()
obj.CityName = "london"
obj.printName("arun")