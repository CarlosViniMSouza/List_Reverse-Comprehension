# 1° -> Criamos uma lista vazia
my_list = []

# Repita os números de 0 a 4 usando a função 'range()', o intervalo 'range(5)' cria um iterável, começando de 0 até (mas não incluindo) 5. Use o método '.append()' para adicionar os números de 0 a 4 à variavel lista denominada 'my_list'.

for num in range(5):
    my_list.append(num)

# Printar my_list
print(my_list)

"""
Output:

[0, 1, 2, 3, 4]
"""


# Iniciar lista de números:
numbers = [1, 2, 3, 4, 5, 6]

# Crie uma nova lista vazia para manter seus quadrados
square_numbers = []

# Iterar sobre a lista inicial, multiplicar cada número por si mesmo, usar o método '.append ()', para adicionar o quadrado à nova lista square_numbers(pt-br: números_quadrados)

for num in numbers:
    square_numbers.append(num * num)

# print new list
print(square_numbers)

"""
Output:

[1, 4, 9, 16, 25, 36]
"""

# Topic -> How to use list comprehension in Python:
new_list = [num for num in range(5)]

print(new_list)

"""
Output:

[0, 1, 2, 3, 4]
"""
