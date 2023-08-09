def insertion(lst):
    # Search entries in lst starting with index 1
    for element in lst[1::]:
        # save index of element
        index = lst.index(element)
        # While the index is positive and the entry to the left is greater than element
        while index > 0 and lst[index-1] > element:
            # replace greater with lesser
            lst[index] = lst [index-1]
            # decrement index
            index -= 1
        # replace lesser with greater
        lst[index] = element
    return lst




#The code below will test your function. If your function
#works, it will print: [1, 2, 3, 4, 5].
print(insertion([5, 1, 47, 3, 2, 4]))