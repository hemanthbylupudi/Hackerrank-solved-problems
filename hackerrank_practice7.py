if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_list=[]
    for i in arr:
        if i not in new_list:
            new_list.append(i)
    a=(sorted(new_list,reverse=True))
    print(a[1])
