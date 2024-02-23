#função com passagem de parâmetro e sem retorno
def soma_2(n1, n2) :
    soma = n1 + n2
    print(soma)
#Tirar da identação
soma_2(2,4)

#função com passagem de parâmetro e com retorno
def media():
    n1 = 2
    n2 = 3
    return (n1+n2)/2
resultado = media()
if resultado >= 6:
    
    print("Aprovado", resultado)
else:
    print("Reprovado")
    
    
#função com passagem de parâmetro e com retorno
def calculaMedia(n1, n2, n3):
    return (n1+ n2 +n3)/3

resultado_2 = calculaMedia(7,7,7)
if resultado_2 >= 6:
    print("Aprovado", resultado_2)
else:
    print("Reprovado", resultado_2)
