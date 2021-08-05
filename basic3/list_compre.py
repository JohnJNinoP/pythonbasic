def run():
    squart = []
    for i in range(1,101):
        if(i%3) != 0:
            squart.append(i**2)


    squart_comprehemsions = [i**2 for i in range(1,101) if i%3 !=0 ]

    multi = [i for i in range(1,100000) if i%4 ==0 and i%6 ==0 and i%9 ==0] 

    dic = { i:i**2 for i in range(1,101)  }


    print(squart)
    print(multi)

    print(dic)

    palabra = lambda string : string == string[::-1]

    print(palabra("ana"))

if __name__ == '__main__':
    run()