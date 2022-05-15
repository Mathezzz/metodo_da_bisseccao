import numpy as np
#/Use as funções do numpy para criar as funções problemas/
#/Utilize np.sqrt(termo) para a raiz quadrada do termo////

#Definindo a função matemática que será analisada
#Função testada:
#def f(x): return x**3 -6*x
def f(x): return x**2-3.9
#Definindo os valores do intervalo
intervalo_inferior = -2.0
intervalo_superior = 2.0
step=0.5

e=0.0001  #precisão desejada na solução
limite=10 #limite de iterações

#Passar o valor do intervalo para ser trabalhado por duas outras variáveis
a= intervalo_inferior
b= intervalo_superior
c=step


#Definindo a função que irá achar o valor da raiz após isolar pelo teorema de bolzano
def aproximador(valor1, valor2):
    iteracao=0
    while (abs((valor2-valor1)/2)>e):
        xi=(valor1+valor2)/2                        #método da bisecção
        #print("Iteração:", iteracao+1, " xi:", xi)  #Descomentar esta linha caso ver o valor a cada iteração
        iteracao=iteracao+1
        if (iteracao==limite):
            break
        if (f(xi)==0):
            return xi
            break
        else:
            if (f(valor1)*f(xi)<0):
                valor2=xi
            else:
                valor1=xi
    return xi

#/Separação de intervalos de bolzano
raiz_no_ponto=None
for ponto in np.arange(a, b, c):
    if f(ponto)==0:
        print("intervalo:", a, " <-> ", ponto, "  |  Raiz: ", a)
    #if f(ponto)==0:
    #   raiz_no_ponto = ponto
    #    print("intervalo: ", a, " <-> ", ponto, "  |  Raiz: ", raiz_no_ponto)
    else:
        if f(a)*f(ponto)<0:                 #Se o teorema verdadeiro
            raiz=aproximador(a,ponto)       #A raiz é o valor retornado da função aproximação com o intervalo como parâmetro
            print("intervalo: ", a, " <-> ", ponto, "  |  Raiz aprox: ", raiz)
    print(a, ponto)
    a=ponto
if f(ponto)*f(b)<0:                 #Se o teorema verdadeiro
            raiz=aproximador(ponto, b)       #A raiz é o valor retornado da função aproximação com o intervalo como parâmetro
            print("intervalo: ", ponto, " <-> ", b, "  |  Raiz aprox: ", raiz)
if f(b)==0:
        print("intervalo:", ponto, " <-> ", b, "  |  Raiz: ", b)