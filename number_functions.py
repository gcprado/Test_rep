def dif_even_odd(values_1: list, values_2: list) -> tuple:
    """
    Sum two list of the same range item by item and
    returns a list containing a tuple that in his
    even index (i = 0) shows how many even sums where made,
    and in the odd index (i = 1) how many odds where made.
    
    The last value of the list (an integer) shows
    the module (positive value) of the difference
    between the two values obtanied inside the tuple;
    
    For e.g:
    # input:  A = [3, 5, 4, 3, 6]
    #         B = [2, 3, 5, 8, 2] 
    # output: C = [(2, 3), 1]
    """
    evens = 0
    odds = 0
    for value_1, value_2 in zip(values_1, values_2):
        add = value_1 + value_2
        if add % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    if evens >= odds:
        dif = evens - odds
    else:
        dif = odds - evens
    
    pair = (evens, odds)
    output = []
    output.append(pair)
    output.append(dif)
    return output
