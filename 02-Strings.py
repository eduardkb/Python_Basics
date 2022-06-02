

# ############################################################################
print(f"{'':#<50}")
print(f"{' Funçao Len ':#^50}")
print(f"{'':#<50}")

usuario = "Eduard Buhali"
qtd_caractes = len(usuario)
print(f'{usuario} contém {qtd_caractes} caracteres.')

# ############################################################################
print(f"{'':#<50}")
print(f"{' Converter para string ':#^50}")
print(f"{'':#<50}")

i = 50
s = str(i)
print(f'Original type: {type(i)} | After convering with str(): {type(s)}')

# ############################################################################
print(f"{'':#<50}")
print(f"{' Índices ':#^50}")
print(f"{'':#<50}")

nome = "Eduard Keller Buhali EKB"
print("String manipulada abaixo:", nome)
print("Indice 2 da string: ", nome[2])
print("Indice -1 da string: ", nome[-2])
print(f'Removendo ultimo caracter: {nome[:-1]}')
print(f'Peager texto do meio: {nome[3:6]}')
print(f'Do começo: {nome[:3]}')
print(f'Do fim: {nome[22:]}')
print(f'Com step: {nome[7:20:2]}')

# ############################################################################
print(f"{'':#<50}")
print(f"{' Split e Join ':#^50}")
print(f"{'':#<50}")

text = "Eduard Keller Buhali EKB"
print("String manipulada abaixo:", nome)
lista = text.split(' ')
print("String split:", lista)
rejoin = ';'.join(lista)
print("String joined with ';':", rejoin)

# ############################################################################

print(f"{'':#<50}")
print(f"{' find and replace ':#^50}")
print(f"{'':#<50}")

sTxt = "The quick brown fox jumps over the lazy dog. The fox is fast."
print("The original text:", sTxt)
print("find() result for 'dog':", sTxt.find("dog"))
print("find() result for 'unknown':", sTxt.find("unknown"))

print("replace() result for 'fox':", sTxt.replace("fox", "monkey"))
