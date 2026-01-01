def dijkstra_algo(CM, i=0):
    n = len(CM)
    # 初始化
    S = [0]*n
    Dist = CM[i].copy()
    # 起點i
    S[i] = 1
    Dist[i] = 0
    while(sum(S)<n): # 尚有節點的最短路徑未被確定
        # 從未被確定的節點中找出最短路徑的下一個節點
        min_value = float('inf')
        min_k = -1
        for k in range(n):
            if(S[k]==0 and Dist[k]<min_value):
                min_value = Dist[k]
                min_k = k
        # 設定節點 k 被確定
        S[min_k] = 1
        
        # 因為節點 min_k 被確定後，更新各點可能因為經過節點 min_k 而產生的最短路徑
        for k in range(n):
            d = Dist[min_k] + CM[min_k][k] # 試算 Vi-->Vmin_k-->Vk之距離
            if(d<Dist[k]): # 從 Vi 到 Vk 經過 Vmin_k 會更短
                Dist[k] = d
                
        print(Dist)
        print(S)
        print('')
    return Dist