# function definition and palindrome example
import re
print('\n\n\n#####################################################')


def palindrome(sEntry):
    sEntry = (re.sub('\W+', '', sEntry)).lower()
    sInv = ''
    for i in range(len(sEntry) - 1, -1, -1):
        sInv += sEntry[i]

    print(f"String: {sEntry} | Inverted: {sInv}")
    return True if sEntry == sInv else False


# sInput = "aibofobias"
# sInput = "Eduard Buhali"
# sInput = "Omissíssimo!"
sInput = "Anotaram a data da maratona."
sRes = "Yes" if palindrome(sInput) else "No"

print("Is '{}' a palindrome? {}".format(sInput, sRes))

print('\n\n\n#####################################################')

# defining function with default parameter names and force str return


def greeting(msg="Olá", name="Eduard") -> str:
    return f'{msg}, {name}!!!'


print(greeting(name="Laysa"))

print('\n\n\n#####################################################')
# Funçao em uma variavel


def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


div = divisao
print(divisao(8, 2))

print('\n\n\n#####################################################')
# Funçao Lambda


def a(x, y): return x * y


print(f'Valor multiplicado pela funçao lambda: {a(3, 4)}')
