"""Implementar uma solução que some todos os números pares de uma lista
    Por exemplo se uma lista for[10,2,5,7,6,3],o resultado deve ser igual a 18"""

lista = [10,2,5,7,6,3]
n = len(lista)
soma = 0
for i in range(n):
    if(lista[i]%2==0):
      soma=soma+lista[i]
print(f'O somatório dos elementos pares da lista é: {soma}')