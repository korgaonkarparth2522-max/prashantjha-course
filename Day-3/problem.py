arr = [-1, 2, -3, 4, 5, -6]

pos = []
neg = []

# Separate positives and negatives
for num in arr:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)

# Merge: negative first
result = []
i = j = 0

while i < len(neg) and j < len(pos):
    result.append(neg[i])
    result.append(pos[j])
    i += 1
    j += 1

# Add remaining elements
while i < len(neg):
    result.append(neg[i])
    i += 1

while j < len(pos):
    result.append(pos[j])
    j += 1

print(result)