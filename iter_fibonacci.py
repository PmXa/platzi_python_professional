import time

class FibonacciIter:
    """ Iterator of the Fibonacci sequence
    """

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.sum = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.sum
            self.n1, self.n2 = self.n2, self.sum
            self.counter += 1
            return self.sum

# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    fibonacci = FibonacciIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.05)


if __name__ == '__main__':
    run()