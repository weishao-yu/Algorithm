n = int(input())
mat = []
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
start = int(input())
def BFS(mat, start):
    visited = [0] * len(mat)
    queue = [start]
    while queue:
        node = queue.pop(0)
        if visited[node] == 0:
            print(node, end=' ')
            visited[node] = 1
        for j in range(len(mat)):
            if mat[node][j] == 1 and visited[j] == 0:
                queue.append(j)
BFS(mat, start)