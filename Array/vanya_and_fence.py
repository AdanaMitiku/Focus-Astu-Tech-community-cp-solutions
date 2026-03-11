n,h=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n):
    if l[i]<=h:
        l[i]=1
    else:
        l[i]=2
print(sum(l))   

