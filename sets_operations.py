# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    my_set1 = {1, 2, 3, 4}
    my_set2 = {4, 5, 6, 7}

    union = my_set1 | my_set2
    print(union)

    intersection = my_set1 & my_set2
    print(intersection)

    difference = my_set1 - my_set2
    print(difference)

    symmetric_difference = my_set1 ^ my_set2
    print(symmetric_difference)


if __name__ == '__main__':
    run()