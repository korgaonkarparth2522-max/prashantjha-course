# input = "aaabbbcccc"
# a = ""
# for i in input:
#     if i not in a:
#         a += i
#         a += str(input.count(i))
# print(a)

#WAP to reverse each word in a string
s = "Hello World"
a = s.split()
print(a)

b = ""
for i in a:
    b += i[::-1] + " "
print(s)
print(b)
