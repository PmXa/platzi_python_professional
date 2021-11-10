"""
Hola 3 -> HolaHolaHola
Platzi 4 -> PlatziPlatziPlatziPlatzi
"""

def make_repeater_of(n: int):

    def repeater(string: str) -> str:
        assert type(string) == str, "Sólo se admiten cadenas de texto"
        return string*n

    return repeater

# Main function & entry point

def run():
    repeat_5 = make_repeater_of(5)
    repeat_9 = make_repeater_of(9)

    print(repeat_5("Tengo"))
    print(repeat_9("Hambre"))


if __name__ == '__main__':
    run()