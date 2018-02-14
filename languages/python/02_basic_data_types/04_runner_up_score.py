if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    arr.sort(key=int)
    print(arr[-2])