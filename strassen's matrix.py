import numpy as np

def strassen(a, b):
    # Get the size of the input matrices
    n = len(a)
    
    # Base case for 1x1 matrix multiplication
    if n == 1:
        return a * b

    # Divide matrices into submatrices
    k = n // 2
    a11, a12, a21, a22 = a[:k, :k], a[:k, k:], a[k:, :k], a[k:, k:]
    b11, b12, b21, b22 = b[:k, :k], b[:k, k:], b[k:, :k], b[k:, k:]

    # Compute the 7 products
    m1 = strassen(a11 + a22, b11 + b22)
    m2 = strassen(a21 + a22, b11)
    m3 = strassen(a11, b12 - b22)
    m4 = strassen(a22, b21 - b11)
    m5 = strassen(a11 + a12, b22)
    m6 = strassen(a21 - a11, b11 + b12)
    m7 = strassen(a12 - a22, b21 + b22)

    # Combine the results into resulting submatrices
    c11 = m1 + m4 - m5 + m7
    c12 = m3 + m5
    c21 = m2 + m4
    c22 = m1 - m2 + m3 + m6

    # Combine submatrices into the final result matrix
    c = np.zeros((n, n), dtype=int)
    c[:k, :k] = c11
    c[:k, k:] = c12
    c[k:, :k] = c21
    c[k:, k:] = c22

    return c

# Example usage:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = strassen(a, b)
print("Result of Strassen's Multiplication:")
print(result)
