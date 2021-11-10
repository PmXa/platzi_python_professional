def decorador(func):
    def wrapper():
        print("-" * 24)
        print("Extra: esto no estaba en la función original 📰")
        func()
        print("-" * 24)
    return wrapper

def saludo():
    print("Hola!")


# Main function & entry point
def run():
    saludo()

    salute = decorador(saludo)
    salute()


if __name__ == '__main__':
    run()