from typing import List

def remove_duplicates(some_list: List) -> List:
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    without_duplicates.sort()
    return without_duplicates

# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    a_list = [1, 1, 5, 8, 9, 9, 9, 3 ,6, 4, 8, 6, 1, 5, 1, 1, 2, 4, 6, 5, 9, 7, 8, 6, 5, 4, 2, 1, 4]
    b_list = remove_duplicates(a_list)
    print(b_list)


if __name__ == '__main__':
    run()