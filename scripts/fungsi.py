
def penjumlahan(A,B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matriks harus memiliki ukuran yang sama.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def pengurangan(A,B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matriks harus memiliki ukuran yang sama.")
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def perkalian(A,B):
    if len(A[0]) != len(B):
        raise ValueError("Jumlah kolom matriks A harus sama dengan jumlah baris matriks B.")
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def inverse(A,B):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def transpose(A,B):
    if len(A) != 2 or len(A[0]) != 2:
        raise ValueError("Hanya mendukung matriks 2x2.")
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]