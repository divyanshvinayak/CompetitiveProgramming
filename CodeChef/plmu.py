T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    X = 0
    Y = 0
    for j in range(N):
        if A[j] == 0:
            X += 1
        elif A[j] == 2:
            Y += 1
    print(X * (X - 1) // 2 + Y * (Y - 1) // 2)