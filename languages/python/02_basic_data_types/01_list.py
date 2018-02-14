if __name__ == '__main__':
    N = int(input())
    lst = []
    for item in range(N):
        line = input().split(' ')
        command = line
        if command[0] == 'insert':
            lst.insert(int(line[-2]), int(line[-1]))
        if command[0] == 'remove':
            lst.remove(int(line[-1]))
        if command[0] == 'append':
            lst.append(int(line[-1]))
        if command[0] == 'sort':
            lst.sort()
        if command[0] == 'pop':
            lst.pop()
        if command[0] == 'reverse':
            lst.reverse()
        if command[0] == 'print':
            print(lst)