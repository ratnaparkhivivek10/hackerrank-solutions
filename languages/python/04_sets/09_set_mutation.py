nA = int(input())
A = set(map(int, input().split(' ')))
n_other_sets = int(input())

for _ in range(n_other_sets):
    command, *n = input().split(' ')
    elements = set(map(int, input().split(' ')))
    if command == 'intersection_update':
        A.intersection_update(elements)
    if command == 'update':
        A.update(elements)
    if command == 'difference_update':
        A.difference_update(elements)
    if command == 'symmetric_difference_update':
        A.symmetric_difference_update(elements)
        
print(sum(A))