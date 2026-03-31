n,k=map(int,input().split())
m=list(map(int,input().split()))
diff=0
for i in range(n-k+1):
    a=m[i:k+i]
    b=len(set(a))
    diff=max(diff,b)
print(diff)
