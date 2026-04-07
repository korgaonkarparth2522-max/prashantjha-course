input = [10,98,23,33,12,22,21,11]
new = []
old = []

for i  in input:
    if i % 2 == 0:
        new.append(i)
    else:
        old.append(i)
    
print(sorted(new))
print(sorted(old))
print(new + old)