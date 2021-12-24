# Lista reversa do Python - como reverter um intervalo ou matriz

## Artigo por: Dionysia Lemonaki

![logo_Article](https://www.freecodecamp.org/news/content/images/size/w2000/2021/11/markus-winkler-Q2J2qQsoYH8-unsplash.jpg)

## Neste tutorial, você aprenderá algumas das diferentes maneiras de reverter listas e intervalos de listas em Python. E veremos alguns exemplos de codificação ao longo do caminho.

### Vamos começar!

## Como criar um intervalo em Python:

### Uma maneira eficiente de criar uma lista de um intervalo de números em Python é usar a função interna `range()`.

### Para criar uma lista com um intervalo de números, você usa o construtor `list()` e, dentro dele, a função `range()`.

### A função de intervalo leva até três parâmetros - os parâmetros de `start, stop, and step`, com a sintaxe básica parecida com esta:

`range(start, stop, step).`

### O parâmetro de `start` é o número a partir do qual a contagem começará.

### O parâmetro de `step` é o número até - mas não incluindo - aquele em que a contagem terminará.

### O parâmetro da `step` é o número que determina como os números serão incrementados.

### Dos três parâmetros, apenas a `stop` é necessária e o resto é opcional.

### Se você incluir apenas o parâmetro `stop`, lembre-se de que, por padrão, a contagem começa em 0 e, em seguida, termina um número antes do que você especificou.

### Por exemplo:

```python
# Cria uma lista de números que começa em 0 e termina em 3, não em 4.
my_range = list(range(4))

print(my_range)

"""
Output:

[0, 1, 2, 3]
"""
```

### Então, aqui está como você colocaria tudo isso junto para criar uma lista de um intervalo de números:

```python
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
```

## Como reverter um intervalo em Python:

### Para reverter um intervalo de números em Python com a função `range()`, você usa uma etapa negativa, como `-1`.

### O exemplo abaixo cria uma lista de um intervalo de números começando de 9 até, mas não incluindo, -1 (então a contagem para em 0) e a contagem da sequência é diminuída em 1 a cada vez:

```python
my_range = list(range(9, -1, -1))

print(my_range)
"""
Output:

[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

print(type(my_range))
# Output: <class 'list'>
```

### Ao reverter uma lista, você precisa incluir os parâmetros de `start` e `step`.