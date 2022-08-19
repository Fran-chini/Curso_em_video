'''
Variaáveis compostas!

Tuplas ()- São imutáveis, ou seja, dentro do programa, a forma que ela é criada é a mesma que será usada até o final
Listas[]
Dicionários{}

'''
#Criando tuplas
#Tuplas são imutáveis
lanche = ('Hámburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, lanche):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
for comida in lanche:
    print(f'Vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')



