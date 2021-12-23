# Compreensão de lista em Python

## Artigo por: Dionysia Lemonaki

![logo_Article](https://www.freecodecamp.org/news/content/images/size/w2000/2021/11/christian-wiediger-WkfDrhxDMC8-unsplash.jpg)

### As listas são um recurso útil e frequentemente usado em Python.

### E a compreensão de lista oferece uma maneira de criar listas enquanto escreve um código mais elegante e fácil de ler.

### Neste artigo para iniciantes, darei uma visão geral de como funciona a compreensão de listas em Python. Também mostrarei muitos exemplos de código ao longo do caminho.

## Como usar um loop `for` para criar uma lista em Python:

### Uma maneira de criar uma lista em Python é usando um loop `for`.

### Por exemplo, você pode usar a função `range()` para criar uma lista de números de 0 a 4.

```python
# 1° -> criamos uma lista vazia
my_list = []

# Repita os números de 0 a 4 usando a função 'range()', o intervalo 'range(5)' cria um iterável, começando de 0 até (mas não incluindo) 5. Use o método '.append()' para adicionar os números de 0 a 4 à variavel lista denominada 'my_list'.

for num in range(5):
    my_list.append(num)

# printar my_list
print(my_list)

"""
Output:

[0, 1, 2, 3, 4]
"""
```

### E se você já tiver uma lista de números, mas quiser criar uma nova lista com seus quadrados?

### Você poderia usar novamente um loop `for`, assim:

```python
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
```

### Mas existe uma maneira mais rápida e sucinta de alcançar os mesmos resultados - usando a compreensão de lista.