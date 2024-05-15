# Reverse List
def reverse_list(lst):
    """Reverse the given list.

    Args:
    lst (list): The list to be reversed.

    Returns:
    list: The reversed list.
    """
    return lst[::-1]


# Remove Duplicates
def remove_duplicates(lst):
    """Remove duplicates from the given list.

    Args:
    lst (list): The list from which duplicates are to be removed.

    Returns:
    list: A list with duplicates removed.
    """
    seen = set()
    unique_lst = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_lst.append(item)
    return unique_lst


# Concatenate Lists
def concatenate_lists(lst1, lst2):
    """Concatenate two lists.

    Args:
    lst1 (list), lst2 (list): Lists to be concatenated.

    Returns:
    list: The concatenated list.
    """
    return lst1 + lst2


# List Intersection
def list_intersection(lst1, lst2):
    """Find the intersection of two lists.

    Args:
    lst1 (list), lst2 (list): Lists whose intersection is to be found.

    Returns:
    list: A list of common elements.
    """
    set1 = set(lst1)
    set2 = set(lst2)
    return list(set1 & set2)


# Testing the functions
if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]
    print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # Output: [1, 2, 3, 4]
    print(concatenate_lists([1, 2], [3, 4]))  # Output: [1, 2, 3, 4]
    print(list_intersection([1, 2, 3, 4], [2, 4, 6]))  # Output: [2, 4]
