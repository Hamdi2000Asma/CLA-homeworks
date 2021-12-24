#Q1
from os import X_OK, error


student_nam =open("C:/Users/Timgad informatique/Desktop/CLA-homeworks/student_names.txt","r+")
#Q2
names =["\njoujou","\nnadia","\nsalah","\nmohammed","\nrami"]
student_nam.writelines(names)
#Q3
n = int(input("enter a number : "))
for i in range(0,n):
    print(student_nam.readline())
li=student_nam.readlines()
for i in range(1,n+1):
    print(li[-i])
try:
    print(li.index("asma\n"))
except ValueError as err:
    print(err)
student_nam.close()
a = open("C:/Users/Timgad informatique/Desktop/a.txt","w")
b = open("C:/Users/Timgad informatique/Desktop/b.txt","w")
c=open("C:/Users/Timgad informatique/Desktop/c.txt","w")
d=open("C:/Users/Timgad informatique/Desktop/d.txt","w")
e=open("C:/Users/Timgad informatique/Desktop/e.txt","w")
f=open("C:/Users/Timgad informatique/Desktop/f.txt","w")
g=open("C:/Users/Timgad informatique/Desktop/g.txt","w")
h=open("C:/Users/Timgad informatique/Desktop/h.txt","w")
i=open("C:/Users/Timgad informatique/Desktop/i.txt","w")
j=open("C:/Users/Timgad informatique/Desktop/g.txt","w")
k=open("C:/Users/Timgad informatique/Desktop/k.txt","w")
l=open("C:/Users/Timgad informatique/Desktop/l.txt","w")
m=open("C:/Users/Timgad informatique/Desktop/m.txt","w")
n=open("C:/Users/Timgad informatique/Desktop/n.txt","w")
o=open("C:/Users/Timgad informatique/Desktop/o.txt","w")
p=open("C:/Users/Timgad informatique/Desktop/p.txt","w")
q=open("C:/Users/Timgad informatique/Desktop/q.txt","w")
r=open("C:/Users/Timgad informatique/Desktop/r.txt","w")
s=open("C:/Users/Timgad informatique/Desktop/s.txt","w")
t=open("C:/Users/Timgad informatique/Desktop/t.txt","w")
u=open("C:/Users/Timgad informatique/Desktop/u.txt","w")
v=open("C:/Users/Timgad informatique/Desktop/v.txt","w")
w=open("C:/Users/Timgad informatique/Desktop/w.txt","w")
x=open("C:/Users/Timgad informatique/Desktop/x.txt","w")
y=open("C:/Users/Timgad informatique/Desktop/y.txt","w")
z=open("C:/Users/Timgad informatique/Desktop/z.txt","w")