from typing import Container


def run():
    for cotador in range(1000):
        if cotador % 2 != 0:
            continue
        print(cotador)
        

if __name__ == '__main__':
    run()