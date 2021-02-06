''' Given an integer array, contruct another integer array whose i-th element is the sum of the i-th element
and following i elements. 
For example, a given [3, 6, 2, 7, 8, 5, 4, 1] outputs to a new array [3, 8 (6 + 2), 18 (2 + 7 + 9), 
25 (7 + 9 + 5 + 4), 19 (9 + 5 + 4 + 1)]'''

# x is the int array input


x = [3, 6, 2, 7, 9, 5, 4, 1]
z = 1
sa = []
j = 0
for i in range(len(x)):
    v = 0
    j = i
    while j < (i + z):
        if j != len(x):
            v += x[j]
            j += 1
        else:
            break
    sa.append(v)
    if j != len(x):
        z += 1
    else:
        break
print(sa)
# Or you could return sa if this were a function
