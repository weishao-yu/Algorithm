def floyd_warshall_algo(num, matrix, start, end):
    A = [[0 for b in range(num)] for a in range(num)]
    # 當 k = 0 (初始化)
    for i in range(num):
        for j in range(num):
            A[i][j] = matrix[i][j]
    # 接下來 k=0~n-1
    for k in range(num):
        for i in range(num):
            for j in range(num):
                # 從i節點到j節點必經k節點下的成本
                d = A[i][k] + A[k][j]
                if(d < A[i][j]): # 試試看如果必經k節點會不會更好
                    A[i][j] = d
    return A[start][end]
while True:
    try:
        num = int(input())
        matrix = []
        for i in range(num):
            row = []
            row_input = input().split()
            for j in row_input:
                if j == 'x':
                    row.append(float('inf'))
                else:
                    row.append(int(j))
            matrix.append(row)
        start, end = map(int,input().split())
        result = floyd_warshall_algo(num, matrix, start, end)
        print(result)
        # for row in result:
        #     output_row = []
        #     for val in row:
        #         if val == float('inf'):
        #             output_row.append('x')
        #         else:
        #             output_row.append(str(val))
        #     print(" ".join(output_row))
    except EOFError:
        break