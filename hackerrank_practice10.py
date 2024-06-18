width = int(input())
l = "H"

for i in range(width):
    if width == 2*i+1: a = i-2

for i in range(width):
    st = l*(2*i+1)
    print(st.center(2*width-1," "))
for i in range(3*width - a):
    if i<width+1 or i>(3*width - a)-(width+2):
        s1 = " "*int(width/2) + l*width + " "*3*width + l*width
        print(s1)
    else:
        s2 = " "*int(width/2) + l*width*5
        print(s2)
for i in range(width):
    st = l*(2*width-1 - 2*i)   
    print(" "*(width*4-1),st.center(2*width-1," "))  
