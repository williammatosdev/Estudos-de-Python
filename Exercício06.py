"""Implementar uma solução em que resolva a seguinte questão:
    - Se nota for maior ou igual a 7,o estudante foi aprovado.
    - Se a nota for 7 e maior ou igual a 5,o estudante está em recuperação.
    - Se a nota for menor que 5,o estudante está reprovado"""

media = 8.5

if(media>=7.0):
        situacao = 'aprovado'
elif(media>=5.0):
        situacao = 'recuperação'
else:
    situacao = 'reprovado'

print(f'O estudante está: {situacao}')
    