import copy

def bound_estimate(mat, path):
    # 1. 複製矩陣
    mat_ = copy.deepcopy(mat) 
    N = len(mat_)      
    n = len(path)      
    pool = list(range(N)) 
    
    v = 0 # 累積成本估算值

    # 2. 處理已經走過的路徑
    for i in range(n-1):
        if path[i] in pool:
            pool.remove(path[i]) # 移除已拜訪城市
        
        # 累加已知路徑成本
        v += mat_[path[i]][path[i+1]] 
        
        # 【修正重點在此！】
        # 封鎖回頭路：只有在「不是最後一步」的時候才封鎖
        # 如果 n == N (代表這條路徑已經包含所有城市了)，
        # 當 i == n-2 時 (正在處理最後一條邊)，我們允許它連回起點 path[0]
        if not (n == N and i == n-2):
            mat_[path[i+1]][path[0]] = float('inf') 

    # 3. 處理矩陣封鎖 (Marking Visited)
    # 把剩下的候選池整理出來 (所有沒在 path 裡的點，加上 path 最後一個點)
    # 因為 path 最後一個點還可以當作起點出發去別的地方
    actual_pool = []
    for x in range(N):
        if x not in path[:-1]: 
            actual_pool.append(x)
            
    # 將已訪問過的行 (Column) 設為無限大
    for k in actual_pool: 
        for j in range(1, n): 
            mat_[k][path[j]] = float('inf') 

    # 4. 貪婪估算剩餘成本 (Heuristic)
    # 針對每一個還可以出發的點，找它們的最小出邊
    for k in actual_pool:
        min_ = min(mat_[k]) 
        
        # 如果有死路，代表這條路徑無效
        if min_ == float('inf'): 
            return float('inf')
            
        v += min_ 

    # 5. 特殊處理 (老師原程式碼的這段其實已經包含在上面的迴圈邏輯裡了，
    # 但為了保險起見，若 pool 只剩起點時的處理邏輯通常依靠 Heuristic 自動完成)
    
    return v

def TSP_BB(A, s):
    N = len(A)
    L = list(range(N))
    L.remove(s)
    
    # 初始狀態
    sol = [-1]*(N+1)
    sol.append(float('inf')) 
    
    try:
        lower_bound = bound_estimate(A, [s])
    except:
        lower_bound = 0
    
    # Priority Queue
    priority_queue = [([s], L, 1, lower_bound)] 
    
    while len(priority_queue) > 0:
        path, to_visit, depth, lower_bound = priority_queue.pop()
        
        # [剪枝] 如果估算下界已經比已知最佳解還差，直接放棄
        if lower_bound >= sol[-1]:
            continue

        # --- [終止條件] ---
        if depth == N: 
            # 嘗試回到原點
            back_cost = A[path[-1]][s]
            if back_cost < float('inf'):
                path = path + [s]
                
                # 計算實際總成本
                cost = 0
                for i in range(N):
                    cost += A[path[i]][path[i+1]]
                
                # 更新最佳解
                if cost < sol[-1]:
                    # 這裡修正一下 sol 的存法，只存最後結果比較簡單
                    sol = path + [cost]
                    # 更新 sol[-1] 為 cost 以便剪枝
                    # 注意：原本的 sol 是一個 list，最後一項是 cost
                    # 我們要確保 sol[-1] 隨時都是目前的最小成本
            continue
                
        # --- [擴展節點] ---
        # 收集所有可能的下一步
        next_moves = []
        
        for k in range(len(to_visit)):
            next_node = to_visit[k]
            last_node = path[-1]
            
            # 檢查是否有路
            if A[last_node][next_node] < float('inf'):
                new_path = path + [next_node]
                new_to_visit = to_visit[:k] + to_visit[k+1:]
                
                # 計算新路徑的下界
                new_lb = bound_estimate(A, new_path)
                
                # 只有當下界 < 目前最佳解，才加入 Queue
                if new_lb < sol[-1]:
                    next_moves.append((new_path, new_to_visit, depth+1, new_lb))
        
        # 排序：由大到小排 (因為 pop 是取最後一個)
        next_moves.sort(key=lambda x:x[3], reverse=True)
        priority_queue.extend(next_moves)
                    
    # 回傳結果修正
    if sol[-1] == float('inf'):
        return -1
    else:
        return sol[-1] # 題目只要輸出成本

# --- 主程式區 ---
while True:
    try:        
        N = int(input())
        
        matrix = []
        for i in range(N):
            row_str = input().split()
            row_data = []
            for char in row_str:
                if char == 'x':
                    row_data.append(float('inf'))
                else:
                    row_data.append(int(char))
            matrix.append(row_data)
        
        # 執行計算
        # TSP 通常從 0 開始
        print(TSP_BB(matrix, 0))
        
    except EOFError:
        break