import numpy as np

W = [
    [1, 0, 0],
    [2, -2, 0],
    [2, 0, -2],
    [3, -3, -3]
]

def fizz_buzz(n : int) -> str:
    w = np.array(W)
    v = np.array([1, n % 3, n % 5])
    labels = [str(n), "fizz", "buzz", "fizzbuzz"] 
    idx = np.argmax(w @ v)
    return labels[idx]


for i in range(1, 101): 
    print(fizz_buzz(i))