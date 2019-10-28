
class Person:
  def __init__(self, fname, lname):
    print("Person __init__")
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print("printname")
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    print("Student __init__")
    Person.__init__(self, fname, lname)
    self.firstname = fname+"_Student"
    self.lastname = lname+"_Student"

  def printname_Student(self):
    print("printname_Student")
    print(self.firstname, self.lastname)

class Student2(Student):
  def __init__(self, fname, lname):
    print("Student2 __init__")
    Student.__init__(self, fname, lname)
    self.firstname2 = fname+"_Student2"
    self.lastname2 = lname+"_Student2"

  def printname_Student2(self):
    print("printname_Student2")
    print(self.firstname2, self.lastname2)

x = Student2("Mike", "Olsen")
x.printname()
x.printname_Student()
x.printname_Student2()

