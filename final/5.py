def function(price, weight, limit):
    num = len(price)
    dp = [[0 for i in range(limit + 1)] for j in range(num + 1)]
    for i in range(1, num + 1):
        curr_price = price[i - 1]
        curr_weight = weight [i - 1]
        for j in range(1, limit + 1):
            if curr_weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                up = dp[i - 1][j]
                take = dp[i -  1][j - curr_weight] + curr_price
                dp[i][j] = max(up, take)
    return dp[num][limit]
while True:
    try:
        price = list(map(int, input().split())) 
        weight = list(map(int, input().split()))
        limit = int(input())
        best = function(price, weight, limit)
        print(best)
    except EOFError:
        break