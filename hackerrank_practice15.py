# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))
res = a^b
print(len(res))
