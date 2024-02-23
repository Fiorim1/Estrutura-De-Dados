array = ["S", "A", "T", "C"]
print(array[0])
print(array[1])
print(array[2])
print(array[3])
array[1] = "B"
print(array)
for elemento in array:
    print(elemento)
    #len(array): len() é uma função em Python que retorna o comprimento de um objeto iterável, como uma lista. Neste caso, 
    # len(array) retorna o comprimento da lista array, que é o número de elementos que ela contém.
for index in range(len(array)):
    # print(array[index])
    #Indíce serve para 
    print(index)
    #Em resumo, index é uma variável que representa a posição de cada elemento na lista enquanto percorremos a lista usando o loop for. 
    # É como se fosse o "número da vez" enquanto estamos olhando para cada elemento da lista um por um.
    