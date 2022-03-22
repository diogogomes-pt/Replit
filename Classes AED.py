print ("teste")

class BagWithList(object):
    def __init__(self):
        self.collection = list()

    def add(self, item):
        self.collection.append(item)

    def size(self):
        return len(self.collection)

    def is_empty(self):
        return len(self.collection) == 0

    def __iter__(self):
        return iter(self.collection)


print("Bag")

myBag2 = BagWithList()
myBag2.add(2)
print(myBag2.is_empty())
myBag2.add(19)
myBag2.add(74)
myBag2.add(23)
myBag2.add(19)
myBag2.add(12)

print("fim")


myBag = BagWithList()
myBag.add(2)
print(myBag.is_empty())
myBag.add(19)
myBag.add(74)
myBag.add(23)
myBag.add(19)
myBag.add(12)

value = int(input("Qual o valor que esta no Bag "))
if value in myBag:
    print("Bag contem esse valor", value)
else:
    print("Bag não contem esse valor", value)




class BagWithList(object):
  def __init__(self):
    self.collection = list()

  def add(self, item):
    self.collection.append(item)

  def size(self):
    return len(self.collection)

  def is_empty(self):
    return len(self.collection) == 0

  def __iter__(self):
    return iter(self.collection)

print ("Bag")



class Employee:   
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee" + Employee.empCount )
     #print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

##---mainn
     
emp = Employee ("zara", 200)
emp.displayEmployee()


emp2 = Employee ("carro", 200)
emp2.displayEmployee()


print ("Total Employee %d", Employee.empCount)
