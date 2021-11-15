import time

def fibo_gen(limit: int = -1):
    """ 
    Generator for Fibonacci numbers:\n
    \tfibo_gen()  => Generates Fibonacci sequence number indefinitely\n
    \tfibo_gen(n) => Generates the first <n> Fibonacci numbers
    """
    n1 = 0
    n2 = 1
    counter = 0

    while (limit < 0) or (counter < limit):
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            counter += 1
            aux = n1 + n2
            n1, n2 = n2, aux
            yield aux

# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    fibonacci = fibo_gen(10)

    for element in fibonacci:
        print(element)
        time.sleep(0.15)


if __name__ == '__main__':
    run()