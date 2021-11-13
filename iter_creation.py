class EvenNumbers:
    """ Iterator of:
        (a) all even numbers
        (b) all even numbers up to a maximum
    """

    def __init__(self, max = None) -> None:
        self.max = max

    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if not (self.max) or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    even_numbers = EvenNumbers(20)
    for number in even_numbers:
        print(number)


if __name__ == '__main__':
    run()