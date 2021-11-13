import time
from typing import List


def log_to_file(mode: str = "w"):
    """ Decorator to log the return statement of a function to a text file
    """
    def write_to_file(func):
        def wrapper(*args, **kwargs):
            f_name = func.__name__
            date = time.strftime("%Y-%m-%d (%H:%M)")
            filename = str(f_name) + " @ " + date
            with open(filename, mode, encoding="utf-8") as file:
                result = func(*args, **kwargs)
                file.write(str(result))
        return wrapper
    return write_to_file


@log_to_file()
def print_multiples(number: int, limit: int = 100) -> List[int]:
    multiples = [i for i in range(limit + 1) if (i % number == 0)]
    return multiples


@log_to_file()
def beautify_text(message):
    better_message = f"💖{message}💖"
    return better_message

# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    print_multiples(7,150)
    beautify_text("Holi")


if __name__ == '__main__':
    run()