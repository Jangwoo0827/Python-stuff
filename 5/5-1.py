for i in range(1,6):
    print(i, end=' ')
print('')
for j in range(1,6):
    print(6-j, end=' ')
print('')
for k in range(1, 11):
    if k%2 == 0:
        print(k, end=' ')
print('')
for l in range(1, 10):
    if l%2 == 1:
        print(l, end=' ')
print('')
z = int(input("ENTER A NUMBER:"))
for x in range(1, z*3+1):
    print(x, end=' ')