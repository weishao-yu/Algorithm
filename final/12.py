def dijkstra_algo(N, matrix, start, end):
    S = [0] * N
    Dist = matrix[start].copy()
    S[start] = 1
    while sum(S) < N:
        min_value = float('inf')
        min_k = -1
        for k in range(N):
            if S[k] == 0 and Dist[k] < min_value:
                min_value = Dist[k]
                min_k = k
        S[min_k] = 1
# 【關鍵修改】如果找不到下一個可到達的點 (min_value 還是 inf)，就跳出
        if min_k == -1 or min_value == float('inf'):
            break    
        for k in range(N):
            d = Dist[min_k] + matrix[min_k][k]
            if d < Dist[k]:
                Dist[k] = d
    if Dist[end] == float('inf'):
            return -1
    else:
        return Dist[end]
while True:
    try:
        N = int(input())
        matrix = []
        for i in range(N):
            row_input = input().split()
            row = []
            for item in row_input:
                if item == 'x':
                    row.append(float('inf'))
                else:
                    row.append(int(item))
            matrix.append(row)
        start, end = map(int, input().split())
        result = dijkstra_algo(N, matrix, start, end)
        print(result)
    except EOFError:
        break
