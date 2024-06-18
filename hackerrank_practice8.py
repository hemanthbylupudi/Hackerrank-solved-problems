if __name__ == '__main__':
    new_list=[]
    grades=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        new_list.append([name,score])
        grades.append(score)
    new_grades=[]
    for i in grades:
        if i not in new_grades:
            new_grades.append(i)
    a=(sorted(new_grades)) 
    names=[]
    low_grade= a[1]
    for i in new_list:
        if i[1]==a[1]:
            names.append(i[0])
    names.sort()
    for i in names:
        print(i)
