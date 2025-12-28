def LIS_compute(x):
    n =len(x)
    dp = n * [1]
    for i in range(1, n):  
        for j in range(i):
            if x[i] >= x[j]:
                dp[i] = max (dp[i], dp[j] + 1)    
    return max(dp)
while True:
    try:
        x = list(map(int, input().split()))
        result = LIS_compute(x)
        print(result)
    except EOFError:
        break