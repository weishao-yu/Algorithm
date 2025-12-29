def hamilton_cycle(matrix):
    n = len(matrix)
    path = [-1] * n
    
    # 策略：固定從第 0 個節點出發
    path[0] = 0 
    
    visited = [False] * n
    visited[0] = True # 起點已走過

    # 呼叫遞迴
    if solve_hamilton(matrix, path, 1, visited):
        return True
    else:
        return False

def solve_hamilton(matrix, path, pos, visited):
    n = len(matrix)
    
    # --- Base Case: 填滿了 n 個位置 ---
    if pos == n:
        last_node = path[pos-1]
        start_node = path[0]
        
        # 檢查最後一個點能不能回到起點
        if matrix[last_node][start_node] == 1:
            return True
        else:
            return False

    # --- 遞迴嘗試 ---
    for v in range(1, n):
        prev_node = path[pos-1]
        
        # 檢查：有路 (==1) 且 沒走過 (visited==False)
        if matrix[prev_node][v] == 1 and visited[v] == False:
            
            # 做決定
            path[pos] = v
            visited[v] = True
            
            # 遞迴
            if solve_hamilton(matrix, path, pos + 1, visited) == True:
                return True
            
            # Backtracking (反悔)
            visited[v] = False
            path[pos] = -1
            
    return False

while True:
        try:
    # 【修正 1】讀取 N 的方式
            line = input().split()
            if not line: break # 防止空行
            N = int(line[0])   # 取 list 的第 0 個元素轉 int
            
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
            
            # 執行並印出結果
            print(hamilton_cycle(matrix))
        except EOFError:
            break