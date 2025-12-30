# 設計一函式 LIS_compute()，其功能為計算輸入序列其 最長遞增子序列 (Longest Increasing Subsequence) 的長度，並輸出。
# Input format 輸入一行數個數字，數字以空格隔開。
# Output format 輸出最長遞增子序列的長度。
# Sample input
# 4 2 2 5 3 7
# Sample output
# 4
#上課教學:一個序列的「最長遞增子序列 (LIS)」，其實就是「原本序列」與「排序後的序列」的「最長公共子序列 (LCS)」。
# 遞減數列 直接a = sorted(x, reverse=True)
# 嚴格的話 sorted(list(set(x)))
def LIS_compute(x):
    a = sorted(x, reverse=True)
    nX = len(x)
    table = [[0 for i in range(nX + 1)] for j in range(nX + 1)]
    for i in range(1, nX + 1):
        for j in range(1, nX + 1):
            if x[i - 1] == a[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[nX][nX]
while True:
    try:
        x = list(map(int, input().split()))
        print(LIS_compute(x))
    except EOFError:
        break
# 若要求字串 直接把之前寫好的 get_LCS_content(seq1, seq2) 拿來用，把 seq2 換成 sorted(seq1) 丟進去，回傳出來的就是 LIS 的內容。