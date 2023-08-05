def max_frequency(lst):
    freqs = {}
    for item in lst:
        if item in freqs.keys():
            freqs[item] += 1
        else:
            freqs[item] = 1
    return max(freqs, key=freqs.get)
