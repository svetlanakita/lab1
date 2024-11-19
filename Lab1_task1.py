numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

p = 0
q = 0
for i in range(len(numbers)):
    if(numbers[i] is None):
        p = i
    else:
        q+=numbers[i]
numbers[p] = (q/(len(numbers)))
print("Changed list:", numbers)
