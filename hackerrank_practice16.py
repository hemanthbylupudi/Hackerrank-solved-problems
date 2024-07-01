# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))
res1=b.difference(a)
res2=a.difference(b)
res=list(res1.union(res2))
for i in sorted(res):
    print(i)
