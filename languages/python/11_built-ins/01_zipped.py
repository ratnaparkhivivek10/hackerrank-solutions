n, x = list(map(int, input().split(' ')))
[print(sum(item)/x) for item in zip(*[map(float, input().split(' ')) for _ in range(x)])]