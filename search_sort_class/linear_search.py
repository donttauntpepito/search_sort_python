

def linear(list_to_search, search_for):
    for i in range(len(list_to_search)):
        if list_to_search[i] == search_for:
            return i
    return False    



a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6))



