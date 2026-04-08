# Dict = {"B":2,"A":1,"C":3}
# Asc = sorted(Dict.items())
# Des = sorted(Dict.items(),reverse=True)
# Asc = dict(Asc)
# Des = dict(Des)
# print("Ascending Order by key:",Asc)
# print("Descending Order by Value:",Des)

#expected ascending output : {"A": 1, "B":2, "C":3}
#expected descending output : {"C: 3, "B":2, "A":1}

#-----------------------------------------------------------------------

# input = {"A": 1, "B": 2, "C":3}
# input.clear()
# print(input)

#-----------------------------------------------------------------------

# a = {"A": 1, "B": "", "C": 3, "D": None, "E": "Five"}
# nonempty = 0
# for i,j in a.items():
#     if i!= "" and j!= "":
#         nonempty += 1
# print(nonempty)   