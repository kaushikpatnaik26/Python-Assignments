def print_tuple_sum(outer_tuple):
    for inner_tuple in outer_tuple:
        sum = 0
        for element in inner_tuple:
            sum += element
        print(sum , end = ' ')

tuple_ = ((1, 2, 3), (4, 5, 6), (5, 6, 8), (4, 8, 10))
print_tuple_sum(tuple_)