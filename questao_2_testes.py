from questao_2_funcoes import *

# Validação letra a)
print('Validação letra a)')
familias = ['MHmm', 'HMhm', 'MHmmh', 'HMhmhhmhm', 'HM', 'HMm', 'MH']
for familia in familias:
    print(f'Família: {familia.ljust(20)} - Válida: {arranjo_letra_a(familia)}')
print()

# Validação letra b)
print('Validação letra b)')
familias = ['MHm', 'HMhm', 'MHmmhm', 'HMhmhhmhm', 'HM', 'MHhhhmhm', 'MHhhh']
for familia in familias:
    print(f'Família: {familia.ljust(20)} - Válida: {arranjo_letra_b(familia)}')
print()

# Validação letra c)
print('Validação letra c)')
familias = ['MH', 'HMmh', 'MHmmh', 'HMmhhmhmhmhmmhhmmh', 'HMmm', 'MHhhhmhm', 'MHhhh']
for familia in familias:
    print(f'Família: {familia.ljust(20)} - Válida: {arranjo_letra_c(familia)}')
print()

# Validação letra d)
print('Validação letra d)')
familias = ['MMmhmmmmh', 'HHhmhmmhmmh', 'HHmhhmmh', 'MHmhhmmh', 'MMmmh', 'HMmm', 'HHmmhmhh']
for familia in familias:
    print(f'Família: {familia.ljust(20)} - Válida: {arranjo_letra_d(familia)}')
print()

# Validação letra e)
print('Validação letra e)')
familias = ['MMmhmhmhm', 'HHhmhm', 'HHmhmhmh', 'MMhmhmh', 'MMmmh', 'HMmm', 'HHhmhmhmm']
for familia in familias:
    print(f'Família: {familia.ljust(20)} - Válida: {arranjo_letra_e(familia)}')
print()

# Validação letra f)
print('Validação letra f)')
familias = ['MMm', 'HHh', 'HHmmhm', 'MMhmh', 'MMmhmhmhmhh', 'HMhmhhmh', 'HHhhmhhhmh']
for familia in familias:
    print(f'Família: {familia.ljust(20)} - Válida: {arranjo_letra_f(familia)}')
print()

# Validação letra g)
print('Validação letra g)')
print('Você terá que digitar os valores de X e Y para cada teste para determinar se a quantidade de adultos está dentro do intervalo permitido.\n')
familias = ['MMm', 'MHMh', 'HHMMHmmhmmm', 'HMHMHMhmh', 'MHM', 'MHMmhmhmhmhh', 'Hhmhhmh', 'MHhhmhhhh']
for familia in familias:
    print(f'Família: {familia.ljust(20)} - Válida: {arranjo_letra_g(familia)}\n')
print()
