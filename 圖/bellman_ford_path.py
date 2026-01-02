def bellman_ford_path(num, matrix, start, end):

    # Dk 表格: 距離
    Dk = [[float('inf') for b in range(num)] for a in range(num)]
    
    # 【新增】 P 表格: 路徑來源 (Parent)
    # P[k][v] 存的是: 第 k 輪走到 v 時，它的前一個點是誰
    P = [[-1 for b in range(num)] for a in range(num)]

    Dk[0][start] = 0
    # P[0][start] = -1 (起點沒有爸爸)

    # --- k = 1 初始化 ---
    for j in range(num):
        Dk[1][j] = matrix[start][j]
        # 如果起點可以直接走到 j，那 j 的爸爸就是 start
        if matrix[start][j] != float('inf'):
            P[1][j] = start

    # --- DP 迴圈 (k = 2 ~ n-1) ---
    for k in range(2, num):
        for v in range(num):
            # 1. 先繼承上一輪的結果 (預設不換路)
            Dk[k][v] = Dk[k-1][v]
            P[k][v] = P[k-1][v]  # <--- 爸爸也繼承

            # 2. 嘗試鬆弛
            for u in range(num):
                if (u != v and matrix[u][v] < float('inf')):
                    d = Dk[k-1][u] + matrix[u][v]
                    
                    # 如果發現走 u 這條路更近
                    if d < Dk[k][v]:
                        Dk[k][v] = d
                        P[k][v] = u  # <--- 【關鍵】 記錄我是從 u 來的！

    # --- 輸出處理區 ---
    
    # 情況 1: 走不到
    if Dk[num-1][end] == float('inf'):
        return "No Path"
    
    # 情況 2: 回溯路徑 (Backtracking)
    path = []
    curr = end
    
    # 從終點往回找，直到找到起點 (-1 代表沒路了或到頭了)
    # 我們查最後一輪 (num-1) 的 P 表格即可
    while curr != -1:
        path.append(curr)
        if curr == start: # 找到起點就停止
            break
        curr = P[num-1][curr] # 查表：誰帶我來的？
    
    # 檢查：如果回溯完了卻沒回到 start (可能是孤兒點)，也是無路
    if path[-1] != start:
        return "No Path"

    # 因為是從 end 加到 start，所以要反轉
    return path[::-1]

# --- 測試區 ---
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
        
        # 印出結果
        print(bellman_ford_path(num, matrix, start, end))
        
    except EOFError:
        break