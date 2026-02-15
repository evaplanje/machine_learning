import numpy as np

# Matrix maken
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(A[0, 1])

A[0, 0]= 73
print(A)
A[0, 1] = 10
print(A)

A[1, 2] = 22
