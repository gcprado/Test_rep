# Test_rep

As said in the function documentation is a simple test_program that:

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

--There are two sets of even sums: (5 + 3, 6 + 2)
and thre sets of odd sums: (3 + 2, 4 + 5, 3 + 8);
1 is the modular difference between 3 and 2
    
