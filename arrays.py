from array import *

#utilizando a biblioteca padrão array do python
my_array = array('i', [1,2,3,4]) #criando um array utilizando a biblioteca array (array.('i') significa que estou declarando um array do tipo )

my_array.insert(2, 6) #usando o método insert para inserir o número 6 no índice 2
print(my_array)

#Traversing an array ("Atravessando um array")

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.2, 2.4, 8.7, 9.8])

arr1.insert(2, 9)
print(arr1)

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)

#Acessando um elemento do array
def acessarElemento(array, index):
    if (index > len(array) ):
        print("Não há um elemento com esse index!")
    return array[index]

print("Elemento do arr1: ", acessarElemento(arr2, 3))