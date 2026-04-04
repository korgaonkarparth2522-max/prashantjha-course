input = {"X": 20, "Y": 10, "Z": 30}

for i, j in input.items():
    if j == min(input.values()):
        print(i)