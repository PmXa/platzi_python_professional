def with_custom_message(message):
    def with_message(function):
        print(f"{message}:")
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
        return wrapper
    return with_message


@with_custom_message("Hello!")
def int_multiply(a: int,b: int) -> int:
    c: int = a * b
    print(f"{a}×{b} = {c}")


# Main function & entry point
def run():
    int_multiply(10, 20)


if __name__ == '__main__':
    run()