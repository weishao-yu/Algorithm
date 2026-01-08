def get_all_stack(data):
    result = []
    def dfs(data, stack, output):
        if not data and not stack:
            result.append(output)
            return
        if data:
            dfs(data[1:], stack + [data[0]], output)
        if stack:
            dfs(data, stack[:-1], output + [stack[-1]])
    dfs(data, [], [])
    return result
def solve(data, target):
    result = get_all_stack(data)
    n = 0
    for i in result:
        if i[0] == target:
            n += 1
    return n
while True:
    try:
        data = input().split()
        target = input()
        print(solve(data, target))
    except EOFError:
        break