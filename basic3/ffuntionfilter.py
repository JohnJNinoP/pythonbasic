from functools import reduce

# funcion filter

my_list = [1,4,5,6,9,13,19,21]
inpares = list(filter(lambda x: x%2  != 0,my_list))
print(inpares)



def pares(number):
    if number % 2 == 0:
        return True
    return False

def elevado(number):
    return number **2 
print(list(filter(pares,my_list)))


# funcion map
my_listmap = [1,2,3,4,5]


print([i**2 for i in my_listmap])
print(list(map( lambda x: x**2, my_listmap )))
print(list(map(elevado,my_listmap)))

# funcion reduce

my_list_reduce = [2,2,2,2,2]

value = 1

for i in my_list_reduce:
    value = value *i
print(value)

print(reduce(lambda a,b : a*b , my_list_reduce))

