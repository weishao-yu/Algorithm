# 找出 LCS 本體 (Printing LCS)
# Input:
# 3 1 4 1 5 9 2 6
# 1 4 1 4 2 1 3 5
# Output:
# [1, 4, 1, 5] (或是其他的合法 LCS)
def get_LCS_content(seq1, seq2):
    nX = len(seq1)
    nY = len(seq2)
    table = [[0 for j in range(nY + 1)] for i in range(nX + 1)]
    for i in range(1, nX + 1):
        for j in range(1, nY + 1):
            if seq1[i - 1] == seq2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    result = []
    i, j = nX , nY
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            result.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    result.reverse()
    return result

while True:
    try:
        seq1 = list(map(int, input().split()))
        seq2 = list(map(int, input().split()))
        print(get_LCS_content(seq1, seq2))
    except EOFError:
        break