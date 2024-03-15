import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def create_matrix(N):
    return [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
    print()

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def multiply_matrix_by_scalar(matrix, scalar):
    return [[scalar * cell for cell in row] for row in matrix]

def matrix_multiplication(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def count_greater_than_K_in_even_columns(E, K):
    count = 0
    for row in E:
        for i in range(1, len(row), 2):  
            if row[i] > K:
                count += 1
    return count

def product_in_odd_rows(D):
    product = 1
    for i in range(0, len(D), 2):  
        for val in D[i]:
            product *= val
    return product

def main():
    K = int(input("Введите число K: "))
    N = int(input("Введите размерность матрицы N: "))

    if N % 2 != 0:
        print("N должно быть четным.")
        return

    A = create_matrix(N)
    print("Матрица A:")
    print_matrix(A)

    mid = N // 2
    B = [row[:mid] for row in A[:mid]]
    C = [row[mid:] for row in A[:mid]]
    D = [row[:mid] for row in A[mid:]]
    E = [row[mid:] for row in A[mid:]]

    if count_greater_than_K_in_even_columns(E, K) > product_in_odd_rows(D):
        E, D = D, E  
    else:
        C, B = B, C  

    F = [B[i] + C[i] for i in range(mid)] + [D[i] + E[i] for i in range(mid)]

    print("Матрица F после преобразований:")
    print_matrix(F)

    AF = matrix_multiplication(A, F)
    KAF = multiply_matrix_by_scalar(AF, K)
    F_transposed = transpose_matrix(F)
    result = matrix_multiplication(KAF, F_transposed)

    print("Матрица AF (A умноженное на F):")
    print_matrix(AF)

    print("Матрица KAF (K умноженное на AF):")
    print_matrix(KAF)

    print("Матрица F транспонированная:")
    print_matrix(F_transposed)

    print("Результат выражения (К(AF))*F^T:")
    print_matrix(result)

if __name__ == "__main__":
    main()

