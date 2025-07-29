class Person:
     def print_name(self,name):
         print("My name is "+name)
     def add(self,a,b):
         return a+b
     def sub(self,a,b):
         return a-b
         
person=Person()
person.print_name("Siva")
result = person.add(3,5)
result = person.sub(5,3)
print(result)