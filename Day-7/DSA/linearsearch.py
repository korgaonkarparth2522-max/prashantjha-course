def linearsearch(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1

array=[1,2,3,4,5,6,7,8]
target=55
result=linearsearch(array,target)
if result==-1:
    print("Element not found")
else:
    print("Element found at index=",result)