a = input()
b = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in b:
    a = a.replace(i, '*')
print(len(a))