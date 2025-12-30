def get_LCString_content(s1, s2):
    n = len(s1)
    m = len(s2)
    table = [[0] * (m + 1) for _ in range(n + 1)]
    
    max_len = 0
    end_index = 0  # 用來記錄最大值發生在 s1 的哪個位置
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
                # 如果發現更長的，記錄長度與結束位置
                if table[i][j] > max_len:
                    max_len = table[i][j]
                    end_index = i
            else:
                table[i][j] = 0
                
    # Python 切片 s1[start : end]
    return s1[end_index - max_len : end_index]

# 測試
print(get_LCString_content("ABABC", "BABCA")) 