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

# Topico -> Como usar a compreensão de lista em Python:
new_list = [num for num in range(5)]

print(new_list)

"""
Output:

[0, 1, 2, 3, 4]
"""

new_list = [num * 2 for num in range(5)]

print(new_list)

"""
Output:

[0, 2, 4, 6, 8]
"""

# Iniciar lista:
numbers = [1, 2, 3, 4, 5, 6]

# nova lista (new list)
# num * num é a operação que ocorre para criar os quadrados

square_numbers = [num * num for num in numbers]

print(square_numbers)

"""
Output:

[1, 4, 9, 16, 25, 36]
"""

# Topico -> Como usar condicionais com compreensão de lista em Python:

new_list = [num for num in range(50) if num % 2 == 0]

print(new_list)

"""
Output:

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
"""

new_list = [num for num in range(50) if num > 20 and num % 2 == 0]

print(new_list)

"""
Output:

[22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
"""
