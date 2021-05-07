# name: Kevin Lin
# date: 02/28/2021
# purpose: create functions that will sort lists

# Parameters: the_list is a list, p and r are integers representing list indices of the_list, and p is less than r
# Parameters: compare_func is a function
# partition will return the index of pivot after sorting an index range defined by p and r
# in an order according to compare_func
def partition(the_list, p, r, compare_func):
    i = p - 1
    j = p
    pivot = the_list[r]

    while j != r:
        if not compare_func(the_list[j], pivot):
            j = j + 1

        elif compare_func(the_list[j], pivot):
            i = i + 1
            the_list[i], the_list[j] = the_list[j], the_list[i]
            j = j + 1

    the_list[r], the_list[i+1] = the_list[i+1], the_list[r]
    return i+1

# Parameters: the_list is a list, p and r are integers representing list indices of the_list, and p is less than r
# Parameters: compare_func is a function
# recursive function that sorts an index range defined by p and r in an order according to compare_func
def quicksort(the_list, p, r, compare_func):
    if r < p + 1:
        return

    q = partition(the_list, p, r, compare_func)
    quicksort(the_list, p, q-1, compare_func)
    quicksort(the_list, q+1, r, compare_func)

# Parameters: the_list is a list, compare_func is a function
# sort will run a sort of the full list
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list) - 1, compare_func)
