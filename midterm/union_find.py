def union_find(edge, P):
    v1, v2 = edge[0], edge[1]
    cycle_exist = False
    if P[v1] == -1 and P[v2] == -1:
        P[v1] = v1
        P[v2] = v1
    elif P[v1] == -1:
        P[v1] = v2
    elif P[v2] == -1:
        P[v2] = v1
    else:
        while P[v1] != v1:
            v1 = P[v1]
        while P[v2] != v2:
            v2 = P[v2]
        if P[v1] == P[v2]:
            cycle_exist = True
        else:
            P[v2] = v1
    return cycle_exist
def is_tree(mat):
    n = len(mat)
    P = [-1] * n
    edge_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if mat[i][j] == 1:
                edge = (i, j)
                edge_count += 1
                if union_find(edge, P):
                    return False

    if edge_count == n - 1:
        return True
    return False

n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
if is_tree(mat):
    print("Tree")
else:
    print("Not a Tree")