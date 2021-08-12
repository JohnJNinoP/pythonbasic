def read():
    numbers = []
    with open('./archivos/numeros.txt','r',encoding="utf-8") as file:
        for i in file:
            try:
                numbers.append(int(i))
            except ValueError:
                numbers.append(i.replace("\n",""))
            
    print(numbers)

def write():
    names = ("john","jairo","arriana","sofia","niño")
    with open('./archivos/name.txt','w',encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    read()
    write()

if __name__ == '__main__':
    run()