"""
class student:
    name="Fathima"
s1=student()
print(s1.name,s1)

class car:
    #parameterised constructor
    def __init__(self,brand,mileage,price):
        self.brand= brand#object attributes
        self.mileage=mileage
        self.price=price
        print("adding the car details")
    color="blue"#class attributes
    model="sedan"
    obj="cars"
    def sayprice(self):
        print("The price is",self.price)
    def welcome(self):
        print("Welcome to ",self.brand)
c1=car("Mercedes",20,"$300k")
print(c1.color,c1.model,c1.brand,c1.mileage,c1.obj)
c1.welcome()
c1.sayprice()
c2=car("BMW",30,"$400k")
print(c2.color,c2.model,c2.brand,c2.mileage,c2.obj)
c2.welcome()
c2.sayprice()

class Student:
    @staticmethod
    def FathersName():
        print("Father's Name is Shameem")
    @staticmethod
    def MothersName():
        print("Mother's Name is Sabina")
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        i=0
        for val in self.marks:
            sum+=val
            i+=1
        print("Hi ",self.name,"Your avg mark is",sum/i)

    
stud1=Student("Maryam",[99,100,98])
stud1.avg()
stud1.FathersName()
stud1.MothersName()
stud2= Student("Fathima",[100,98,98])
stud2.avg()
stud2.FathersName()
stud2.MothersName()

#Abstraction 
class Car:
    def __init__(self):
        self.acc=False
        self.brake= False
        self.clutch=False
        print("Not sarted yet")
    
    def start(self):
        self.clutch=True
        self.brake=True
        print("Car started...")

car1=Car()
car1.start()

#Banking system
class Account:
    def __init__(self,balance,acctno):
        print("Bank account number: ",acctno)
        print("Balance is ",balance)
        self.balance=balance
        self.acctno=acctno
    bankname="SBI"
    def debit(self,amt):
        print("Amount",amt," is been debited")
        self.balance-=amt
        print("Your Balance is ",self.balance)
    def credit(self,amt):
        print("Amount",amt," is been credited")
        self.balance+=amt
        print("Your Balance is ",self.balance)
    def bal(self):
        print("Your Final Balance is ",self.balance)

acc1=Account(1000000,"Ac123456")
acc1.debit(10)
acc1.credit(1000)
acc1.bal()

class hello:
    def __init__(self,name):
        self.name=name
h1=hello("hooi")
print(h1.name)
del h1
print(h1)

class cred:
    def __init__(self,name,password):
        self.name=name
        self.__password=password#private attribute
    def resetpass(self):
        print(self.__password)
    def __secret(self):#private method
        print("this is a secret")
    def toCallPriv(self):
        self.__secret()
data=cred("Fathima","abcdefgh")
print(data.name)
data.resetpass()
data.toCallPriv()
#data.__secret()returns error
#print(data.__password)#returns error

#Inheritence
#Single inher
class Car:
    def __init__(self):
        self.acc=False
        self.brake= False
        self.clutch=False
        print("Not sarted yet")
    
    def start(self):
        self.clutch=True
        self.brake=True
        print("Car started...")
    def stop(self):
        self.acc=False
        self.brake= False
        self.clutch=False
        print("The Car has stopped.")

class toyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand
        print(self.brand)

car1=toyotaCar("Toyota")
car1.start()
car1.stop()
print("\n")
class bmw(Car):
    def __init__(self,name):
        self.name=name
        print(self.name)
        super().start()
    @staticmethod
    def speed():
        print("Speed is 120 km/hr")
    
car2=bmw("X5")
car2.speed()
#multilevel inher
class Fortuner(toyotaCar):
    def __init__(self,type):
        self.type= type
        print(type)
car3=Fortuner("EV")
car3.start()

#Multiple inheritance
class A:
    varA="Welcome to class A"
class B:
    varB="Welcome to class B"
class C(A,B):
    varC="Welcome to class C"

c1=C()

print(c1.varA,c1.varB,c1.varC)

#class method
class People:
    name="anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name=name
    
p1=People()
p1.changeName("Zameel")
print(p1.name)
print(People.name)

class stud:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.math=math
        self.chem=chem
    @property
    def percent(self):
        return str((self.math+self.phy+self.chem)/3)+"%"
stu1=stud(100,10,50)    
print(stu1.percent)

stu1.phy=86
print(stu1.percent)

#polymorphism--operator overloading
print(1+2)
print("hello"+" world")
print([1,2,3]+[4,5,6])

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):#dunderfunct
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return complex(newReal,newImg)

    def __sub__(self,num2):#dunderfunct
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return complex(newReal,newImg)
num1=complex(1,3) 
num1.show()
num2=complex(5,4)
num2.show() 
#num3=num1.add(num2)
num3=num1+num2
num3.show() 
num4=num3-num2
num4.show()

class circle():
    def __init__(self,rad):
        self.rad=rad

    def area(self):
        print("Area is ",3.14*self.rad**2)

    def perimeter(self):
        print("Perimeter is ",3.14*self.rad*2)
cir1=circle(5)
cir1.area()
cir1.perimeter()

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,od2):
        return self.price>od2.price
od1=order("tea",15)
od2=order("samosa",10)
print(od1>od2)
"""
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    
    def showDetails(self):
        print("Role : ",self.role,"\nDept : ",self.dept,"\nSalary : ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT",100000)
        

em1=Engineer("Fathima",20)
em1.showDetails()
