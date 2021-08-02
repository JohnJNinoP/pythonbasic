from typing import Container


def run():
        LIMIT = 1000000
        contador = 2
        while contador < LIMIT:
            contador = (2**contador)
            print(contador)

if __name__ == '__main__':
    run();