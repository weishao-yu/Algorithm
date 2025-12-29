# 核心回溯函式
def maze_solver(matrix, startr, startc, endr, endc):
    n_rows = len(matrix) # 總共有幾個橫條 (高度)
    n_cols = len(matrix[0])# 一個橫條裡有幾個格子 (寬度)
    flag = False
    # 1. Base Case: 到達終點
    if startr == endr and startc == endc:
        return True
    
    # 2. Base Case: 撞到牆壁 (#) 或是 已經走過的路 (非 '_')
    # 注意：程式碼邏輯是檢查是否為 '_' 才進入嘗試，
    # 所以撞牆或回頭路的檢查隱含在 else (return False) 中

    if matrix[startr][startc] == '_':
        # --- 嘗試方向 1: 向右 (Right) ---
        if startc < n_cols - 1:
            matrix[startr][startc] = '>' # 留下足跡
            flag = maze_solver(matrix, startr, startc + 1, endr, endc) # 遞迴往下走
            
        # --- 嘗試方向 2: 向下 (Down) ---
        if flag == False and startr < n_rows - 1:
            matrix[startr][startc] = 'v'
            flag = maze_solver(matrix, startr + 1, startc, endr, endc)
            
        # --- 嘗試方向 3: 向上 (Up) ---
        if flag == False and startr > 0: # 向上            
            matrix[startr][startc] = '^'
            flag = maze_solver(matrix, startr - 1, startc, endr, endc)
            
        # --- 嘗試方向 4: 向左 (Left) ---
        if flag == False and startc > 0: # 向左
            matrix[startr][startc] = '<'
            flag = maze_solver(matrix, startr, startc - 1, endr, endc)
            
        # --- Backtracking 關鍵步驟 ---
        if flag == False:
            # 如果四個方向都走不通，這格是死路
            # 把足跡擦掉，變回 '_' (Backtrack)
            matrix[startr][startc] = '_' 
            
        return flag # 如果 flag 變 True，代表找到路了，一路回傳 True 上去

    else:
        # 可能是牆壁 '#'，或者是剛走過的足跡 (>, v, <, ^)
        return False
    
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
            print('False')
        else:
            result = maze_solver(matrix, startr, startc, endr, endc)
            print(result)
    except EOFError:
        break