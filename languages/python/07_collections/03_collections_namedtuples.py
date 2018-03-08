from collections import namedtuple
from functools import reduce

n = int(input())
columns = input().strip().split()
Student = namedtuple('Student', columns)
studentList = []

for _ in range(n):
    studentList.append(Student(*input().strip().split()))

per = reduce(lambda x, y: x+y, [int(item.MARKS) for item in studentList])/n
print(per)