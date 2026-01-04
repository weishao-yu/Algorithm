# 1. 核心 Backtracking (完全不用改)
def m_coloring(Mat, VC, v, m):
    N = len(Mat)
    if v == N:
        return True # 找到解了
    
    for c in range(1, m + 1):
        flag = True
        for i in range(v):
            if Mat[i][v] == 1 and VC[i] == c:
                flag = False
                break
        
        if flag == True:
            VC[v] = c
            if m_coloring(Mat, VC, v + 1, m) == True:
                return True
            VC[v] = 0 # Backtrack 歸零
            
    return False

# 2. 主程式區塊
while True:
    try:
        N = int(input())
        matrix = []
        for i in range(N):
            row = list(map(int, input().split()))
            matrix.append(row)
        M = int(input())
        
        # 初始化顏色陣列
        VC = [0] * N
        
        # 直接呼叫一次就好，不用迴圈
        if m_coloring(matrix, VC, 0, M) == True:
            print("Yes") # 可以用 m 色著色
        else:
            print("No")  # 不能
            
    except EOFError:
        break