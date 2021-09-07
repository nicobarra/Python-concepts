
def remove_duplicates_with_for(list):
    without_duplicates = []
    for element in list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def set_remove_duplicates(list):
    new_list = set(list)
    return new_list

def run():
    clean_list = remove_duplicates_with_for([1, 2, 2, 3, 3, 4, 5, 6, 6])
    print(clean_list)
    set_list = set_remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5, 6, 6])
    print(set_list)
if __name__=='__main__':
    run()