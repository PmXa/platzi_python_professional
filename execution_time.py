from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        print("-"*32)
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"{time_elapsed.total_seconds()} seconds elapsed")    
        print("-"*32)
    return wrapper


@execution_time
def random_func():
    for _ in range(1_000_000):
        pass


@execution_time
def int_suma(a: int, b:int) -> int:
    print(f"{a} + {b} = {a + b}")
    return a + b


@execution_time
def salute(name = "Napoleón"):
    print("Bonjour, " + name)


# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    random_func()
    int_suma(4, 17)
    salute()


if __name__ == '__main__':
    run()