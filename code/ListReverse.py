# Cria uma lista de números que começa em 0 e termina em 3, não em 4.

my_range = list(range(4))

print(my_range)

"""
Output:

[0, 1, 2, 3]
"""

# Cria uma lista de números que começa em 0 e termina em 3, não em 4.
my_range = list(range(4))

print(my_range)

"""
Output:

[0, 1, 2, 3]
"""

# Cria uma lista de intervalo de números:
# Partindo de 0 até, mas não incluindo, 10 e a contagem é incrementada em 1
my_range = list(range(0, 10, 1))

# Printar no console:
print(my_range)

"""
Output:

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# Verifique o tipo usando o método incorporado type()
print(type(my_range))

"""
Output:

#<class 'list'>
"""

# Topico -> Como reverter um intervalo em Python:

my_range = list(range(9, -1, -1))

print(my_range)
"""
Output:

[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

print(type(my_range))
# Output: <class 'list'>

# Topico -> Como reverter uma lista em Python usando o método .reverse():

# Iniciar lista
my_list = [10, 20, 30, 40, 50]

print("My initial list is: ", my_list)

"""
Output:

My initial list is:  [10, 20, 30, 40, 50]
"""

# Iniciar lista
my_list = [10, 20, 30, 40, 50]

# Invertendo ordem dos itens
my_list.reverse()

print("This is what the list looks like now: ", my_list)

"""
Output:

This is what the list looks like now:  [50, 40, 30, 20, 10]
"""

# Topico -> Como reverter uma lista em Python usando o operador de fatiamento:
my_list = [10, 20, 30, 40, 50]

my_list2 = my_list[1:3:1]

print(my_list2)

"""
Output:

[20, 30]
"""

my_list = [10, 20, 30, 40, 50]

my_list2 = my_list[:]

# ou ...

my_list2 = my_list[::]

# Printar no console
print(my_list2)

"""
Output:

[10, 20, 30, 40, 50]
"""

my_list = [10, 20, 30, 40, 50]

my_list2 = my_list[::-1]

print(my_list2)

"""
Output:

[50, 40, 30, 20, 10]
"""
