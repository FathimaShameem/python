#hello this is a comment 
"""
print("Hello world "," My name is Fathima")
name="Fathima"
age=20
print(name,age)
bool=True
print(bool)
old=None
print(type(old))
txt="@"
print(2*txt*3)#string gets multiplied
a,b="2",3
print((a+txt)*b)
A=1.5
print(b//A)#integer division gives floor value  

name=input("Name :") 
age = int(input("age : "))
price= float(input("price :"))
if(age==12):
    print("Name is ",name,"age is ",age,"Price is ",price)
 
#ternary if variable
food=input("food:")
eat="yes" if food=="cake" else "no"
print(eat)

#ternary statement

food=input("Food ")
print("sweet") if food=="cake" else print("Not sweet")

#ternary clever if
age=int(input("Age is: "))
vote=("yes","no")[age<=18]#first false then true
print(vote)

a=2
b=10
print(a**b)
c=int("68")
print(c+b,type(c))

str="this is a string \nnext line"
print(str,len(str),str[5],str[0:10],str[-3:-1])

str="i am studing"
print(str.endswith("ing"))
print(str.capitalize())
print(str.replace("i","o"))
print(str.find("am"))
print(str.count("i"))

marks=[1,2,3,4,5]
print(marks,type(marks),marks[0:2],marks[-3:-1])
print(marks.append(10),marks.sort(reverse=True),marks.reverse(),marks.insert(5,1))
#the above will give none for all functions
marks.append(10)
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(25,1)
print(marks)
char=['z','d','v','a']
char.sort()
print(char)

tup=(32,90,4,2,4,"hello")
print(tup,type(tup))
print(tup[0:4],tup.index("hello"),tup.count("hello"))

f1=input("enter first movie")
f2=input("enter second movie")
f3=input("enter third movie")
mov=[]
mov.append(f1)
mov.append(f2)
mov.append(f3)
print(mov)

movies=[]
movies.append(input("Enter"))
print(movies)

pal=[1,2,2,1]
pal1=pal.copy()
pal.reverse()
if(pal1==pal):
    print("is a pallindrome")
else:
    print("not pallindrome")

info={
    "name":"fathima",
    "cgpa":8.59,
    "subjects":["python","c","cpp","js"],
    12:12.56
}
print(info,type(info))
print(info["name"])
print(info["subjects"])
print(info[12])

info["name"]="Fathima Shameem"
print(info["name"])

student={
    "name":"Fathima",
    "subjects": {
        "phy":98,
        "chem":100
    },
    "grade":12
}
print(student)
print(student["subjects"]["chem"])
print(student.keys())
print(list(student.values()))
print(student.items())
print(student.get("name"))
new={"place" : "kannur"}
student.update(new)
print(student)

nums={1,2,3,4,4}#4 wont repeat since this is a set
print(nums,type(nums),len(nums))
coll=set()
print(type(coll))
coll.add(1)
coll.add(10)
coll.add("HELLO")
coll.add((1,2,2,4))#tuple
print(coll)
final=nums.union(coll)
print(final)
final2=nums.intersection(coll)
print(final2)

dictionary = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat":"a small animal"
}
print(dictionary)

marks={}

x=int(input("enter the marks "))
marks.update({"PHY" : x})

x=int(input("enter the marks "))
marks.update({"CHEM" : x})

x=int(input("enter the marks "))
marks.update({"MATH" : x})
print(marks)

val={9,"9.0"}
print(val)

value={
    ("float",9.0),
    ("int",9)
}
print(value)

i=1
while i<=100:
    print(i)
    i+=1

i=5
while i>=0:
    print(i)
    i-=1

n=int(input("write the number "))
i=1
while i<=10:
    print(i,"*",n,"=",i*n)
    i+=1
 
i=1
j=1
k=0
new2= []
while i<=10:
    j=i**2
    i+=1
    new2.append(j)
    new2.sort()
print(new2)
while k<10:
    print(new2[k])
    k+=1
l=0
num=int(input("enter the number "))
while l<len(new2):
    if(new2[l]==num):
        print("present at idx ",l)
    l+=1

num=[0,1,2,2,3,4]
for val in num:
    print(val)
str="hi hello how are you"
for el in str:
    print(el)
    if(el=="o"):
        print("O found")
else:
    print("\nend")

seq=range(5)#stop
for i in seq:
    print(seq[i])
for el in range(1,6,2):#start,stop,step
    print(el)

for el in range(2,100,2):#even numb
    print(el)

num=int(input("Number plz "))
for el in range(11):
    pass#for empty loops
    #print(el,"*",num,"=",el*num)

sum=0
i=0
num=int(input("Number plz "))
while i<=num:
    sum+=i
    i+=1
print("Sum is ",sum)

fact=1
num=int(input("Number plz "))
for el in range(1,num+1,1):
    fact*=el
print("fact is ",fact)

def sum(a,b):
    return a+b
print(sum(10,5))

def lenlist(a):
    print(len(a))
new=[1,2,3,4,5,6,7]
lenlist(new)

city=["kannur","kochi","chennai","delhi"]
def printOneLine(a):
    for el in a:
        print(el, end=" ")
printOneLine(city)

def usd_inr(n):
    inr=n*90
    print(inr)
usd_inr(10)

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(10)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

def sumn(n):
    if(n==0):
        return 0
    return n+sumn(n-1)
print(sumn(5))

def print_list(list, id=0):
    if(id==len(list)):
        return
    print(list[id])
    print_list(list, id+1)

no = ["0","1","2"]
print_list(no)
"""


 