# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
b=set()
for i in range(n):
    a=input()
    b.add(a)
print(len(b))
