matrix = []
soma = 0

for i in range(4):
    matrix.append([])
    for c in range(4):
        matrix[i].append([])

for i in range(4):
    for c in range(4):
        matrix[i][c] = int(input('Informe um valor: '))
        if i == c:
            soma += float(matrix[i][c])
print(matrix)
print(f'A soma da diagonal principal da matriz é: {soma}')
