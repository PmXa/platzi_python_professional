def mayus_decorator(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper


@mayus_decorator
def message(name):
    return f'{name}, you have a message.'


# Main function & entry point
def run():
    print(message("Rick"))


if __name__ == '__main__':
    run()