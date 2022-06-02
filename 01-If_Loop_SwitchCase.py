"""
if and loops
"""

# ############################################################################
print("##########"*5)
print("{sep}{sep} {txt} {sep}{sep}".format(txt='IF', sep="#"))
print(f"{'':#<50}")
i = 2
j = 1

if i == 1 or j == 2:
    print("i is", i, sep=": ", end=".")
elif not i == 3:
    print(f'i is equal to {i}')
else:
    print('else')

print("Short if: i = 2") if i == 2 else print("\nShort if: i is not 2")

# ############################################################################
print(f"{'':#<50}")
print(f"{'':#<21} FOR {'':#>22}")
print(f"{'':#<50}")

sText = ''
for i in range(5, 20, 3):  # start, finish (optional), step (optional)
    sText = sText + str(i) + '|'
print(sText)

sText = ''
sTexto = "Python!"
for letra in sTexto:
    if letra == 't':  # pula o 't'
        continue
    if letra == 'n':  # ao encontar o 'n' termina o for
        break
    sText = sText + letra + '|'
print(sText)

sText = ''
for n, letra in enumerate(sTexto):
    sText = sText + str(n) + '-' + letra + '|'
print(sText)

# contador (p = contador. r = range (decrescente))
sText = ''
for p, r in enumerate(range(10, 1, -1)):
    sText = sText + str(p) + '-' + str(r) + '|'
print(sText)
# ############################################################################
print(f"{'':#<50}")
print(f"{'':#<21} WHILE {'':#>22}")
print(f"{'':#<50}")

bContinue = True
i = 0
while bContinue:
    # sNome = input('Digite seu mone: ')
    sNome = "Eu"
    if i == 2:
        sNome = ""
    elif i == 1:
        sNome = "Bu"
 
    if sNome:
        print(f'Seu nome é: {sNome}')
    if sNome == '':
        print('Nenhum nome digitado. Saindo.')
        bContinue = False
    i += 1
# ############################################################################
print(f"{'':#<50}")
print(f"{'':#<21} Switch Case {'':#>22}")
print(f"{'':#<50}")

# ONLY WORKS WITH PYTHON VERSION 3.10+
iHttpErr = 406
match iHttpErr:
    case 400 | 401 | 402:
        print("Standard Error")
    case 404:
        print("Not Found error")
    case 405:
        print("405 error")
    case _:
        print("Unconventional error",iHttpErr)
