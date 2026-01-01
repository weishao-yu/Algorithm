def function(Wi, Vi):
    n = len(Wi)
    cp = []
    for i in range(n):
        ratio = Vi[i] / Wi[i]
        price = Vi[i]
        Weight = Wi[i]
        package = (ratio, price, Weight)
        cp.append(package)
    cp.sort(reverse=True)
    return cp
def Greedy(cp, limit):
    n = len(cp)
    total_price = 0
    for i in range(n):
        if limit >= cp[i][2] :
            total_price += cp[i][1]
            limit -= cp[i][2]
        else:
            remain = limit / cp[i][2]
            total_price += cp[i][1] * remain
            break
    result = round(total_price)
    return  result

while True:
    try:
        Vi = list(map(int, input().split()))
        Wi = list(map(int, input().split()))
        limit = int(input())
        cp = function(Wi, Vi)
        result = Greedy(cp, limit)
        print(result)
    except EOFError:
        break