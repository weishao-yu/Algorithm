def OBST(P_list, Q_list, N):
    P_list = [0] + P_list
    W = [[0 for j in range(N + 1)] for i in range(N + 1)]
    C = [[0 for j in range(N + 1)] for i in range(N + 1)]
    for i in range(N + 1):
        for j in range(i + 1, N + 1):
            C[i][j] = float('inf')
    R = [[0 for j in range(N + 1)] for i in range(N + 1)]
    for k in range(N + 1):
        for i in range(N + 1):
            j = i + k
            if j <= N:
                W[i][j] = Q_list[i]
                for a in range(i + 1, j + 1):
                    W[i][j] += P_list[a] + Q_list[a]
                for b in range(i + 1, j + 1):
                    cost = C[i][b - 1] + C[b][j] + W[i][j]
                    if cost < C[i][j]:
                        C[i][j] = cost
                        R[i][j] = b
    return C[0][N], R
def LDR(R, i, j):
    if i < j:
        r = R[i][j]
        LDR(R, i , r - 1)
        print(r, end= ' ')
        LDR(R, r, j)
def DLR(R, i, j):
    if i < j:
        r = R[i][j]
        print(r, end= ' ')
        DLR(R, i, r - 1)
        DLR(R, r, j)

while True: 
    try:
        N = int(input())
        P_list = list(map(int, input().split()))
        Q_list = list(map(int, input().split()))
        min_cost, R_table = OBST(P_list, Q_list, N)
        print(min_cost)
        LDR(R_table, 0, N)
        print()
        DLR(R_table, 0, N)
        print()
    except EOFError:
        break