def function(price, weight):
    n = len(price)
    cp = []
    for i in range(n):
        r = price[i] / weight[i] 
        p = price[i]
        w = weight[i]
        package = (r, p, w)
        cp.append(package)
    cp.sort (reverse = True)
    return cp

def Greedy(cp, limit):
    n = len(cp)
    total_price = 0
    for i in range(n):
        if limit >= cp[i][2]:
            total_price += cp[i][1]
            limit -= cp[i][2] 
        else:
            remain = limit / cp[i][2]
            total_price += remain * cp[i][1]
            break
    result = round(total_price)
    return result
    
while True:
    try:
        price = list(map(int, input().split()))
        weight = list(map(int, input().split()))
        limit = int(input())
        cp = function(price, weight)
        result = Greedy(cp, limit)
        print(result)
    except EOFError:
        break