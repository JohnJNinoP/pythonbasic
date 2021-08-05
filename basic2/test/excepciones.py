
def divide_elemantos(lista , divisor):
    try:
        return [i/divisor for i in lista]
    except ZeroDivisionError as e:
        return lista


def primeta_letra(lista_palabras):
    primeras_letras = []

    for palabra in lista_palabras:
        assert type(palabra) == str, f'{palabra} no es una srt'
        assert len(palabra) > 0, 'No se permite str vacios'
        primeras_letras.append(palabra[0])
    return primeras_letras

lista = list(range(10))
divisor=0
print(divide_elemantos(lista,divisor))
print(primeta_letra(""))

# Crear un entorno virtual de python 
#py -m venv [nombre]
# alias avenv=.\env\scripts\activate

# pip instalar paquetes dependencias

