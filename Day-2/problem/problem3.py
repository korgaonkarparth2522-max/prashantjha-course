a = []
n = int(input("Enter size of array: "))
for i in range(n):
    val = int(input("Enter element: "))
    a.append(val)
print("Array is: ", a)
sum = 0
for i in range(len(a)-1):
    b=abs(a[i]-a[i+1])
    sum+=b
print("Sum of differences is: ",sum)