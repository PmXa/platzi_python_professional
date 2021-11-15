# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    # Manually creating a set
    my_set1 = {3, 4, 5}
    print("my_set1 = ", my_set1) # my_set1 = {3, 4, 5}

    my_set2 = {"Holi", 23.3, False, True}
    print("my_set2 = ", my_set2) # my_set2 = {False, True, 'Holi', 23.3}

    my_set3 = {3, 3, 2}
    print("my_set3 = ", my_set3) # my_set3 = {2, 3}

    # Error: sets can't contain lists since they are mutable
    # my_set4 = {[1, 2, 3], 4}
    # print("my_set4 = ", my_set4)

    # Set type casting
    my_list = [1, 1, 4, 8, 14]
    my_set = set(my_list)
    print("my_set = ", my_set)

    # Empty set
    empty_set = set()
    print(type(empty_set))

    # Adding elements to sets
    print("empty_set = ", empty_set)

    empty_set.add(1)
    print("empty_set = ", empty_set)

    empty_set.update([1, 2, 3, 4])
    print("empty_set = ", empty_set)

    empty_set.update([1, 5, 6], {7, 8})
    print("empty_set = ", empty_set)

    # Removing elements from sets
    empty_set.discard(7)
    print("empty_set = ", empty_set)

    empty_set.remove(8)
    print("empty_set = ", empty_set)

    empty_set.discard(7)
    print("empty_set = ", empty_set)

    empty_set.remove(8) # Error
    print("empty_set = ", empty_set)

if __name__ == '__main__':
    run()