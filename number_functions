def dif_even_odd(values_1: list, values_2: list) -> tuple:
    """
    Sum two list of the same range item by item and returns a tuple
    containing in the even index (i = 0) how many even sums where
    made, and in the odd index (i = 1) how many odds where made;
    
    For e.g:
    # input:  A = [3, 5, 4, 3, 6]
    #         B = [2, 3, 5, 8, 2] 
    # output: C = (2, 3)
    """
    evens = 0
    odds = 0
    for value_1, value_2 in zip(values_1, values_2):
        add = value_1 + value_2
        if add % 2 == 0:
            evens += 1
        else:
            odds += 1
    output = (evens, odds)
    return output
