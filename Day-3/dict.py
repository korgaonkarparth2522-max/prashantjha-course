mydict ={
    101 : "prashant",
    102 : "ashish",
    "103" : "mohini",
    "104" : "trivani",
    101 : "ashish",
    "pankaj" : "ashish"
}
print(mydict)

# #with the help of key we have to print values
# a = mydict[102] 
# print(a)

# #we will replace old value with new value
# mydict[102] = "peter"
# print(mydict)

# #only print key 
# for i in mydict:
#     print(i)
    
# #only print values
# for i in mydict.values():
#     print(i)
    
# #print key and values both
# for x, y in mydict.items():
#     print(x, y)

# #add new key and value pairs
# mydict["mobile no"] = 9404960916
# print(mydict)

# #pop() method is used to remove the key and value pair from the dictionary
# mydict.pop("103")
# print(mydict)