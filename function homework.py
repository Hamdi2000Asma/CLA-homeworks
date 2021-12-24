#Q1
def palandrom(word):
    l= len(word)
    m=l//2
    d=l-1
    for i in range(0,m):
        if word[i]!=word[d-i]:
            return print("the world is not a palandrom")
    return print("the world is a palandrom")

mot = input("enter a word to check if is alandrom : ")
palandrom(mot)

#Q2
def prim(num):
    for i in range(2,num):
        if num % i == 0 :
            return print("the number is not prime")
    return print("the number is prime")

n = int(input("enter a number to check if prime  : "))
prim(n)
#Q3
def check(a,b,c):
    if a>b and a<c:
        return print("the number is in range")
    elif a<b and a>c:
        return print("the number is in range")
    else:
        return print("the number is not in range")

a=int(input("enter the number checked : "))
b=int(input("enter the first limit of range : "))
c=int(input("enter the second limit of range : "))
check(a,b,c)
#Q4
def fact(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    return print("the factorial of ",a,"is : ",f)
a=int(input("enter the number to calcule the factorial : "))
fact(a)
#Q5
def reverse(s):
    c=""
    l=len(s)-1
    for i in range(l+1):
        c+=s[l-i]
    return print(" the revers word is : ", c)
s=str(input("inter a word to reverse : "))
reverse(s)

#Q6
def somme(l):
    s=0
    for i in l:
        s+=i
    return print("the addition of all the elements of list is : ",s)

l = [1,5,7,3,6,8,2,9,4]
somme(l)

#Q7
def maximum(a,b,c):
    if a>=b and a>=c:
        return print("the max of the tree number is : ",a)
    elif b>=a and b>=c:
        return print("the max of the tree number is : ",b)
    else :
        return print("the max of the tree number is : ",c)
a=int(input("enter the firs number : "))
b=int(input("enter the second number : "))
c=int(input("enter the third number : "))
maximum(a,b,c)


