n = int(input())
mat = []
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
start = int(input())
def DFS(mat, start):
    n = len(mat)
    Visited = [0] * n
    Stack = [start]
    while sum(Visited) < n:
        v = Stack[-1]
        if Visited[v] == 0:
            print(v, end=' ')
            Visited[v] = 1
        go_deeper = False
        for j in range(n):
            if mat[v][j] == 1 and Visited[j] == 0:
                Stack.append(j)
                go_deeper = True
                break
        if not go_deeper:
            Stack.pop()
DFS(mat, start)