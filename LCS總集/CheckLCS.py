# 設計一函式 LCS_check(seq1, seq2, candidate)，其功能為判斷輸入的第三個序列 (candidate) 是否為前兩個序列 (seq1, seq2) 的其中一個最大共同子序列。
# Input format 輸入三行，每行包含數個數字（或字元），以空格隔開。 第一行：序列 A 第二行：序列 B 第三行：候選答案 C
# Output format 如果是其中一個 LCS，輸出 True，否則輸出 False。
# Sample input:
# 3 1 4 1 5 9 2 6 5 3
# 1 4 1 4 2 1 3 5 6 2 3
# 1 4 1 5 2 3
# Sample output
# True
# Sample input:
# 3 1 4 1 5 9
# 1 4 1 9 2 1
# 1 4 1
# Sample output
# False
def LCS(seq1, seq2):
    nX = len(seq1)
    nY = len(seq2)
    table = [[0 for j in range(nY + 1)]for i in range(nX + 1)]
    for i in range(1, nX + 1):
        for j in range(1 , nY + 1):
            if seq1[i - 1] == seq2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j] , table[i][j - 1])
    return table[nX][nY]
def LCS_match(main, seq3):
    index = 0
    num = len(seq3)
    for i in main:
        if i == seq3[index]:
            index += 1
            if index == num:
                return True
    return False
def LCS_check(seq1, seq2, seq3):
    result1 = LCS_match(seq1, seq3)
    result2 = LCS_match(seq2, seq3)
    length = LCS(seq1, seq2)
    result3 = len(seq3) == length
    if result1 and result2 and result3:
        return True
    else:
        return False

while True:
    try:
        seq1 = list(map(int, input().split()))
        seq2 = list(map(int, input().split()))
        seq3 = list(map(int, input().split()))
        print(LCS_check(seq1, seq2, seq3))
    except EOFError:
        break
# 策略
# 條件一： result 必須是 seq1 的子序列 (Subsequence)。
# 條件二： result 必須是 seq2 的子序列 (Subsequence)。
# 條件三： result 的長度必須 等於 seq1 和 seq2 的 LCS 長度。