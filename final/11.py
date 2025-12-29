def maze_solver_optimal(matrix, startr, startc, endr, endc):
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    
    # 1. 邊界檢查：如果起點或終點是牆壁
    if matrix[startr][startc] == '#' or matrix[endr][endc] == '#':
        return 0
        
    # 2. 特殊情況：起點等於終點 (題目定義步數為 1)
    if startr == endr and startc == endc:
        return 1
        
    # 3. 初始化 BFS 佇列 (Queue) --> 【修改點 1】改用一般 List
    # 格式：(列, 行, 目前步數)
    queue = [(startr, startc, 1)]
    
    # 4. 標記起點為已走訪 (變成牆壁 '#')
    matrix[startr][startc] = '#'
    
    # 定義四個方向 (右, 下, 左, 上)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 5. 開始廣度搜尋
    while len(queue) > 0:
        # 【修改點 2】從 List 的第 0 個位置取出 (模擬 popleft)
        curr_r, curr_c, curr_dist = queue.pop(0)
        
        # 檢查終點
        if curr_r == endr and curr_c == endc:
            return curr_dist
            
        # 往四個方向擴散
        for dr, dc in directions:
            next_r, next_c = curr_r + dr, curr_c + dc
            
            # 檢查邊界 + 檢查是否為路 ('_')
            if 0 <= next_r < n_rows and 0 <= next_c < n_cols:
                if matrix[next_r][next_c] == '_':
                    # 標記成牆壁 '#' (代表已走訪)
                    matrix[next_r][next_c] = '#'
                    
                    # 把新座標加入隊伍，步數 + 1
                    queue.append((next_r, next_c, curr_dist + 1))
    
    # 6. 如果隊伍都空了還沒走到終點
    return 0
    
while True:
    try:
        row, col = map(int, input().split())
        matrix = []
        for i in range(row):
            list1 = input().split()
            matrix.append(list1)
        startr, startc = map(int, input().split())
        endr, endc = map(int, input().split())
        if matrix[startr][startc] == '#' or matrix[endr][endc] == '#':
            print('0')
        else:
            result = maze_solver_optimal(matrix, startr, startc, endr, endc)
            print(result)
    except EOFError:
        break