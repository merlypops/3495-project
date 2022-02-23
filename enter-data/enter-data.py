n = int(input("how many values will you provide (integer): "))

list1= []
for i in range(n):
    value=int(input("enter the value: "))
    list1.append(value)

print("list values are: ",list1)