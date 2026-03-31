n = int(input())
b = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    qu = list(map(int, input().split()))
    if qu[0] == 1:
        
        b[qu[1]-1] = qu[2]
    else:
        
        print(b[qu[1]-1])
