# a = {
#     (1,2) : 1, (2,3) : 2, (4,5) : 3
# }
# print(a[(4,5)])

# a = {
#     'a':1, 'b':2, 'c':3
# }
# print(a['a','b'])

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)

# my_dist = {}
# my_dist[1] = 1
# my_dist['1'] = 2
# my_dist[1.0] = 4
# print(my_dist)
# sum = 0
# for k in my_dist:
#     sum += my_dist[k]
# print(sum)

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# print(my_dict)
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
#     print(sum)

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))

# dict = {'c':97, 'a':98, 'b':99}
# for i in sorted(dict):
#     print(i, dict[i])

# rec = {"Name" : "Prashant"}
# r = rec.copy()
# print(id(rec) == id(r))
# print(id(rec))
# print(id(r))

# rec = {"Name" : "Prashant", "Age" : 24, "City" : "Pune", "Country" : "India"}
# id1 = id(rec)
# del rec
# rec = {"Name" : "Prashant", "Age" : 24, "City" : "Pune", "Country" : "India"}
# id2 = id(rec)
# print(id1 == id2)
# print(id(id1))
# print(id(id2))