# mylist = [ [ 'prashant',  'jha' ], [ '85.56' ], [ 440022, "yyy" ] ]      
# print("example of multidimensional list: ")      
# print(mylist)      
# # print(mylist[row][col])   first square bracket represent row and second represent col      
# print(mylist[0][0])      
# print(mylist[0][1])      
# print(mylist[1][0])      
# print(mylist[2][0])      
# print(mylist[2][1])

# list1 = ["prashant","jha"]
# print(list1*3)

# list2 = [50,25,30]
# print(list1+list2)

# list2 = [50,25,"prashant"]
# del list2[2]
# print(list2)

# list2 = [50,25,"prashant"]
# list2.clear()
# print(list2)

# name = "parth"
# print(name)
# myname = list(name) #typecasting
# print(myname)

# mylist = [40,20,50]
# mylist.reverse()
# print(mylist)

# mylist = [40,20,50]
# mylist.sort()
# print(mylist)

# mylist = [44, 22, 77, 0, 9, 88]  
# newlist = mylist  
# print(id(mylist))   
# print(id(newlist)) 
# mylist[0] = "parth"
# print(id(mylist))   
# print(id(newlist))

# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop()) # 4 7 11 15
    
# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1] = arr[i]
#     print(arr[i],end = "")

# a = [1,2,3,4,5,6,7,8,9]
# a[::2] = 10,20,30,40,50,60
# print(a)

# a=[1,2,3,4,5]
# print(a[3:0:-1])

# names = [4,2,5,6,8,2]
# for i in names:
#     print(i)

# A = [4,0,2,5,0,1]
# B = [4,2,5,1,0,0]
# for i in A:
#     if i == 0:
#         A.remove(i)
#         A.append(i)
# print(A)

# A = [1,2,3,4,4,5,2]
# B = []
# for i in A:
#     if i not in B:
#         B.append(i)
# print(B)

# A = [1,2,3]
# B = [2,3,4]
# C = [3,4,5]
# for i in A:  #i = 0:1
#     if i in B and i in C:
#        print(i)