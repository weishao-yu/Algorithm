def insertion_sort(L):
    n = len(L)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if L[j] < L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
            else:
                break 
    return L
while True:
    try:
        L = list(map(int, input().split()))
        result = insertion_sort(L)
        print(*L)
    except EOFError:
        break
