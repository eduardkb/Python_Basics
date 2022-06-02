print('\n#####################################################')
# Convertendo para int
sTest = "25"
sTest = "25a"  # error
sTest = "25.5"  # error
try:
    iNum = int(sTest)
    print(f"CONVERT INT: Numero {iNum} tipo {type(iNum)}")
except:
    print(f"CONVERT INT: It is not possible to convert {sTest} to int.")

# Convertendo para float
sTest = "25"  # CONVERTS OK
sTest = "25.4"  # CONVERTS OK
sTest = "25,4"  # ERROR
sTest = "25,4A"  # ERROR

try:
    iNum = float(sTest)
    print(f"CONVERT FLOAT: Numero {iNum} tipo {type(iNum)}")
except:
    print(f"CONVERT FLOAT: It is not possible to convert {sTest} to int.")

print('\n#####################################################')
# formatando variavel float

nome = 'Eduard'
idade = 36
imc = 77 / (1.83 ** 2)

print(f'Not Formatted IMC: {imc}')
print(f'Formatted IMC: {imc:.3f}')
