n = int(input())
s = set(map(int, input().split()))
a=int(input())
for i in range(a):
    b=input().split()
    if(b[0]=="pop"):
        s.pop()
    elif b[0]=="remove":
        s.remove(int(b[1]))
    elif b[0]=="discard":
        s.discard(int(b[1]))
x=0
for i in s:
    x += i
print(x)
