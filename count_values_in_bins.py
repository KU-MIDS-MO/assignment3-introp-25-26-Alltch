import numpy as np

def count_values_in_bins(data, bin_edges):
    B = len(bin_edges) - 1

    counts = [0] * B

    for x in data:
        if x < bin_edges[0] or x > bin_edges[-1]:
            continue

        for i in range(B):
            left = bin_edges[i]
            right = bin_edges[i + 1]

            if i == B - 1:
                if left <= x <= right:
                    counts[i] += 1
                    break

            else:
                if left <= x < right:
                    counts[i] += 1
                    break

    return np.array(counts, dtype=int)