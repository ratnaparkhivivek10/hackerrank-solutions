data, k = [list(map(int, input().split(' '))) for _ in range(int(input().split(' ')[0]))], int(input())
[print(*row) for row in sorted(data, key=lambda lst: lst[k])]