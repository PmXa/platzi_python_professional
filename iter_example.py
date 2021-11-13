# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    # Manual  sweeping
    my_list = [4, 7, 17, 44, 57]
    my_iter = iter(my_list)

    print(next(my_iter)) # 4
    print(next(my_iter)) # 7
    print(next(my_iter)) # 17

    # Programmatically sweep
    big_list = [i for i in range(100_000) if i%7 == 0]
    big_iter = iter(big_list)

    while True:
        try:
            element = next(big_iter)
            print(element)
        except StopIteration:
            break


if __name__ == '__main__':
    run()