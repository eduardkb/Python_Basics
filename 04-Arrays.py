from random import randint


print('\n#####################################################')
#  array com tipos de dados diferentes
aList2 = ['Civic', 1245, 12.54, True]
print(f'Ultimo valor da lista: {aList2[-1]}')
print(f'Valor no indice 3: {aList2[2]} Tipo de dados: {type(aList2[-2])}')

print('\n#####################################################')
# gerando listas

l2 = list(range(7, 15))  # preencher lista com uma range
print('Lista gerada com multiplos de 7:')
l2 = list(range(0, 100, 7))  # preencher lista pulando numeros
print('lista2:', l2)

print('\n#####################################################')
# ordenando arrays

l3 = [randint(1, 99) for i in range(20)]
# OR:
# l3 = []
# for i in range(20):
#     l3.append(randint(1, 100))

print("Original array:", l3)
l3.sort()
print("Sorted array:", l3)

print('\n#####################################################')
# inserir e remover valores de arrays

l1 = list(range(1, 15))

# adicionar valor com append
print('Adicionar valor 22 no final:')
l1.append(22)
print(l1)

# inserindo em qualquer lugar usando insert
print('Inserir valor 50 na posicao 3:')
l1.insert(3, 50)
print(l1)

# remover último valor com pop
print('Remover ultimo numero com funçao pop:')
l1.pop()
print(l1)

# remover um valor
print('Remover valor na posição 1')
del(l1[1])
print(l1)

# remover valores
print('Remover range de valores (da posição 3 à 6)')
del(l1[3:6])
print(l1)

print('\n#####################################################')
# iterando sobre array com mais dimensoes

lista = [[55, 'Joao', 1.64], [66, 'Maria', 1.55], [77, 'José', 1.98]]

# o for in pode colocar cada valor do array em uma variavel
for indice, nome, altura in lista:
    print(f'"{nome}", com numero de registro "{indice}", tem altura {altura}m.')
