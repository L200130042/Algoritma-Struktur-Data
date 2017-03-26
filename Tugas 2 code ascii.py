def binary_search(lst, search):
    lower_bound = 0
    upper_bound = len(lst) - 1

    while True:
        if upper_bound < lower_bound:
            print("Not found.")
            return -1

        i = (lower_bound + upper_bound) // 2

        if lst[i] < search:
            lower_bound = i + 1
        elif lst[i] > search:
            upper_bound = i - 1
        else:
            print("Element " + str(search) + " in " + str(i))
            return 0
