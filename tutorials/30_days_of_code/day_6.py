N = int(input())

for _ in range(N):
    data = input()
    print('{0} {1}'.format(data[::2], data[1::2]))
