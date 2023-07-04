def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        completed = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(completed[i-1][j-1] + completed[i-1][j])
            row.append(1)
            completed.append(row)

        return completed
