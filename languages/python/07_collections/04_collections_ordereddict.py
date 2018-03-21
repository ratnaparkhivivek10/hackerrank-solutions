from collections import OrderedDict
data = OrderedDict()
for item in [input().rstrip().split(' ') for _ in range(int(input()))]:
    k, v = ' '.join(item[:-1]), int(item[-1])
    data[k] = data.get(k, 0) + v

for k, v in data.items():
    print(k, v)