if __name__ == '__main__':
    N = int(input())
    new_list=[]
    main_list=[]
    for i in range(N):
        a=input()
        new_list.append(a)
    source_list=[]
    for j in range(N):
        b=new_list[j].split(" ")
        source_list.append(b)
    for i in source_list:
        if i[0]=="insert":
            a=int(i[1])
            b=int(i[2])
            main_list.insert(a,b)
        elif i[0]=="print":
            print(main_list)
        elif i[0]=="remove":
            main_list.remove(int(i[1]))
        elif i[0]=="append":
            main_list.append(int(i[1]))
        elif i[0]=="sort":
            main_list.sort()
        elif i[0]=="pop":
            main_list.pop()
        elif i[0]=="reverse":
            main_list.reverse()
            
        
