def remove_duplicates_with_for(list):
    without_duplicates = []
    for element in list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def set_remove_duplicates(list):
    return set(list)

