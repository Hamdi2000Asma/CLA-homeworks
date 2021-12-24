#Q1
list_number=[]
for i in range(1,300):
    list_number.append(i)
#Q2
print(list_number)
print("the length of the list is: ",len(list_number))
for i in range(0,299):
    list_number[i]=list_number[i]**2
print(list_number)
#Q3
print(list_number.index(57))


