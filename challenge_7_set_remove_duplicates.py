from typing import List

def remove_duplicates(some_list: List) -> List:
    without_duplicates = list(set(some_list))
    return without_duplicates

# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    a_list = [1, 1, 5, 8, 9, 9, 9, 3 ,6, 4, 8, 6, 1, 5, 1, 1, 2, 4, 6, 5, 9, 7, 8, 6, 5, 4, 2, 1, 4]
    b_list = remove_duplicates(a_list)
    print(b_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    run()