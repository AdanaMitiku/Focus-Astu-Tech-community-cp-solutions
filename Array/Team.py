
n = int(input())  # number of problems
count = 0

for _ in range(n):
    p, v, t = map(int, input().split())
    if (p not in [0,1]) or (v not in [0,1]) or (t not in [0,1]):
        print("invalid input")
    if p + v + t >= 2:
        count += 1
        

print(count)
