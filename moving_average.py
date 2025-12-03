import numpy as np

def moving_average(signal, window_size):
    if window_size % 2 == 0:
        raise ValueError("Window size must be odd.")
    n = len(signal)
    k = (window_size - 1) // 2

    result = np.zeros(n, dtype=float)

    for i in range(n):
        left = max(0, i - k)
        right = min(n, i + k + 1)
        window = signal[left:right]
        result[i] = np.mean(window)

    return result
