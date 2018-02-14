students = []
grade = {}
std_names = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        grade[name] = score
        
    second_lowest = sorted(list(set(grade.values())), reverse=True, key=float)[-2]
    #print(second_lowest)
    [std_names.append(record[0]) for record in students if record[1] == second_lowest]
    #print(std_names)
    for name in sorted(std_names):
        print(name)