# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = tuple(map(int, raw_input().split(' ')))
polynomial = raw_input()
if(eval(polynomial) == k):
    print(True)
else:
    print(False)