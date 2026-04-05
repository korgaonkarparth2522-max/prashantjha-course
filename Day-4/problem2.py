# num = 578378923
# arr = list(map(int, str(num)))
# print(arr)

# num = [5,7,8,3,7,8,9,2,3]
# b = {}
# print(num)
# count = 0
# for i in num:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# print(b)
# for key, value in b.items():
#     if value > 1:
#         count += 1
# if count > 0:
#     print("Security key is: ", count)
# else:
#     print("Security key is: -1")

#----------------------------------------------------------------------------------------------

# #2nd largest element in the list
# list = [7, 3, 9 , 2, 8]
# list.sort()
# print(list)
# print(list[-2])

#----------------------------------------------------------------------------------------------

# name = "programming"
# vowels = "aeiou"
# new = ""
# cons = ""
# for i in name:
#     if i in vowels:
#         new += i
#     elif i not in vowels:
#         cons += i
# print(new)
# print(cons)
# b = len(new)
# print(b)

#----------------------------------------------------------------------------------------------

# input = [1,2,2,3,4,]
# new = []
# newname = []
# for i in input:
#     if i == 2:
#         new.append(i)
#     else:
#         newname.append(i)
# print(new)
# print("The final list is:", newname)

#----------------------------------------------------------------------------------------------

input = [2,3,4,5]
product = 1
for i in input:
    product *= i
print("The product of the elements in the list is:", product)