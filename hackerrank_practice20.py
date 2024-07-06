def average(array):
    # your code goes here
    a=set(array)
    s=sum(a)
    l=len(a)
    return s/l

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
