from typing import Dict , List
from typing import Tuple

print("Hello")
a = 1
print(type(a))

a: int = 5
print(a)
b : str = 'Hola'
print(b)
c : bool = True
print(c)

def suma(a: int,b:int) -> int:
    return a+b

print(suma(1,5))

positives : List[int] = [1,2,3,4,'5']

users : Dict[str,int] = { 'argentina' : 1,
    'mexico':2,
    'colombia':3
 }

countries : List[Dict[str,str]] = [
     {
        "name":"argentina",
        "people" :"4500000"
     },
     {
         "name":"Mexico",
         "people":"900000"
     },
     {
         "name":"colombia",
         "people":"9999999"
     }
]
print(positives)
print(users)
print(countries) 


numbers : Tuple[int,float,int] = (1,0.5,1)
print(numbers)

coordinatesType : List[Dict[str,Tuple(int,int)]] = [
    {
        'coor1':(1,2),
        'coor2':(3,5)
    },
     {
        'coor1':(0,1),
        'coor2':(2,5)
    }
]
print(coordinatesType)