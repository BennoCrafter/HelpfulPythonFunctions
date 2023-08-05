def max_element(lst):
    j = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > j:
            j = lst[i]

    return j