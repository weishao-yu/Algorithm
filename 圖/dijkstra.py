def dijkstra_algo(num, matrix, start, end):
    # 初始化
    S = [0]* num
    Dist = matrix[start].copy()
    # 起點i
    S[start] = 1
    while(sum(S)<num): # 尚有節點的最短路徑未被確定
        # 從未被確定的節點中找出最短路徑的下一個節點
        min_value = float('inf')
        min_k = -1
        for k in range(num):
            if(S[k]==0 and Dist[k]<min_value):
                min_value = Dist[k]
                min_k = k
        # 設定節點 k 被確定
        S[min_k] = 1
        
        # 因為節點 min_k 被確定後，更新各點可能因為經過節點 min_k 而產生的最短路徑
        for k in range(num):
            d = Dist[min_k] + matrix[min_k][k] # 試算 Vi-->Vmin_k-->Vk之距離
            if(d<Dist[k]): # 從 Vi 到 Vk 經過 Vmin_k 會更短
                Dist[k] = d
    if Dist[end] == float('inf'):
        return -1
    return Dist[end]

while True:
    try:
        num = int(input())
        matrix = []
        for i in range(num):
            row_input = input().split()
            row = []
            for j in row_input:
                if j == 'x':
                    row.append(float('inf'))
                else:
                    row.append(int(j))
            matrix.append(row)
        start, end = map(int, input().split())
        result = dijkstra_algo(num, matrix, start, end)
        print(result)
    except EOFError:
        break
