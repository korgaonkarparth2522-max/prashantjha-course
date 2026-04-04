name =     "prashantjha"
#indexing = 012345678910

print(name[0]) #p
print(name[1]) #r
print(name[-1]) #a
# print(name[15]) #error string index out of name
print(name[0:5]) #start=0 and end=end-1, 5-1=4 =>prash
print(name[1:]) #rashantjha
print(name[:5]) # start=0 and end=5-1=4 =>prash
print(name[1:8:2]) #start=1, end=8-1=7, from ind[1] skip by 2=>rsat
print(name[:]) #prashantjha