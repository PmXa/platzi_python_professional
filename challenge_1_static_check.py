def check_if_prime(number: int) -> bool:
    factors = [x for x in range(1,number) if number%x == 0]
    if len(factors) == 1:
        return True
    else:
        return False


# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    my_num: int = int(input())
    print(check_if_prime(my_num))


if __name__ == '__main__':
    run()