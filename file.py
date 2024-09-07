#FILE I/O
"""
f=open("sample.txt","r")
#data=f.read(10)
print(f.readline())

fp=open("sample.txt","w")
line2=fp.write("this is the second line")
fp.close()

fp=open("sample32.txt","a")
fp.write("\n\nthis is the second line written using append")
fp.close()

with open("demo.txt","r+") as f:
    f.write("this is written using with keyword")
    print(f.read())

#to delete
import os
os.remove("sample.txt")

with open("practice.txt","w+") as fp:
    str=fp.write("Hi everyone\nwe are learningg File I/O\nusing Java.\nI like programming")
with open("practice.txt","r") as fp:
    str=fp.read()
new=str.replace("Java","python")
print(new)
with open("practice.txt","a") as fp:
    fp.write("\n\n")
    fp.write(new)

with open("practice.txt","r") as fp:
    data=fp.read()
    if(data.find("learning")):
        print("learning is present")

def checkforline():
    lineno=1
    with open("practice.txt","r") as f:
        word="learning"
        data=True
        while data:
            data=f.readline()
            if(word in data):
                print(lineno)
            lineno+=1
    
checkforline()
"""
cnt=0 
with open("p1.txt","r") as f:
    data=f.read()
    print(data)

    nums =data.split(",")
    print(nums)
    for val in nums:
        if(int(val)%2==0):
            cnt+=1
print(cnt)
