def make_division_by(divisor):
    """
    This closure returns a function that returns the division of a number by n
    """
    def divider(number):
        return number/divisor

    return divider

# Main function & entry point

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18)) # Expected: 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100)) # Expected: 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54)) # Expected 3


if __name__ == '__main__':
    run()