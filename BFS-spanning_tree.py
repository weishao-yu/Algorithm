def BFS_ST(mat, v = 0):
    n = len(mat)
    ST = [[0 for j in range(n)] for i in range(n)]
    Queue = [(-1,v)]
    Visited = [0] * n
    while sum(Visited) < n:
        p, v = Queue.pop(0)
        if Visited[v] == 0:
            print(v, end=' ')
            Visited[v] = 1
            if p >= 0:
                ST[p][v] = 1
                ST[v][p] = 1
            for j in range(n):
                if mat[v][j] == 1 and Visited[j] == 0:
                    Queue.append((v,j))
    print('')
    return ST
n = int(input())
mat = []
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
start = int(input())
ST = BFS_ST(mat, start)
for row in ST:
    print(' '.join(map(str, row)))