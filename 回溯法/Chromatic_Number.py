# m-Coloring Backtracking
# Mat: 連接矩陣 (Adjacency Matrix)
# VC: Vertex_Color 陣列 (儲存目前的著色結果)
# v: 目前處理的節點 index
# m: 可用的顏色總數

def m_coloring(Mat, VC, v, m):
    N = len(Mat) # 節點總數
    
    # Base Case: 所有節點都著色完成
    if v == N:
        print(VC, 'ok')
        return True
    
    else:
        # 嘗試顏色 1 到 m
        for c in range(1, m + 1):
            flag = True # 預設此顏色合法
            
            # --- 檢查相鄰節點是否有相同顏色 ---
            for i in range(v): # 檢查已經著色過的節點(0 到 v-1)或是檢查所有鄰居
                 # 投影片邏輯：檢查所有節點 i，若有邊且同色則非法
                if Mat[i][v] == 1 and VC[i] == c:
                    flag = False
                    break 
            # --------------------------------
            
            if flag == True: # 如果通過檢查
                VC[v] = c    # 塗色
                
                # 遞迴處理下一個節點 (v+1)
                if m_coloring(Mat, VC, v + 1, m) == True:
                    return True # 找到一組解就回傳，不繼續找
                # 【關鍵修改】: Backtracking 的精隨
                # 如果下面的路走不通 (回傳 False)，要把這裡的顏色清掉！
                VC[v] = 0       
            # 若 flag 為 False，或下一層遞迴回傳 False
            # 則換下一個顏色 (continue loop)
            # 若 loop 結束都沒顏色可用，會自動回傳 None/False (Backtrack)
            
    return False
def solve(Mat):
    n = len(Mat)
    for m in range(1 , N + 1):
        VC = [0] * N
        if m_coloring(Mat, VC, 0, m) == True:
            print(f"最少需要 {m} 種顏色")
            return m # 找到最小的 m 就結束，不用再往下試
            
    return -1

while True:
    try:
        N = int(input())
        matrix = []
        for i in range(N):
            row = list(map(int, input().split()))
            matrix.append(row)
        solve(matrix)
    except EOFError:
        break