while True:
    a = int(input())
    for i in range(a//2):
        print(' ' * (a//2 - i), end = '')
        print('*' * (2*i+1))

    for i in range(a//2-1):
        print(' ' * (i + 2), end = '')
        print('*' * ((a//2*2)-3-2*i))
