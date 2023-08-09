def recursive_binary_search(searchList, searchTerm):
    searchList.sort()

    if len(searchList) == 0:
        return False

    middle = len(searchList) // 2
    
    if searchList[middle] == searchTerm:
        return True
    elif searchTerm < searchList[middle]:
        return recursive_binary_search(searchList[:middle], searchTerm)
    else:
        return recursive_binary_search(searchList[middle + 1:], searchTerm)

intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]

print("23 is in intlist (recursive):", recursive_binary_search(intlist, 23))
print("50 is in intlist (recursive):", recursive_binary_search(intlist, 50))