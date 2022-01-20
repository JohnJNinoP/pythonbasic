def morral(tamano_morral, pesos,valores,n):
    if n == 0 or tamano_morral == 0:
        return 0
    
    if pesos[n-1] > tamano_morral:
        return morral(tamano_morral,pesos,valores,n-1)

    escojo  = valores[n-1] + morral(tamano_morral - pesos[n-1],pesos,valores,n-1)
    noescojo =  morral(tamano_morral,pesos,valores,n-1)
    return max(escojo , noescojo)

    
    

if __name__ =='__main__':
    valores = [60,100,120]
    pesos = [10,20,30]
    tamano_morral = 30
    n= len(valores)

    result = morral(tamano_morral,pesos,valores,n)
    print(result)