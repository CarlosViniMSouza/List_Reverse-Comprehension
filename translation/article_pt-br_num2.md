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

## Como reverter uma matriz em Python:

### Uma matriz na programação é uma coleção ordenada de itens, todos do mesmo tipo de dados.

### Cada item da coleção possui seu próprio número de índice.

### No entanto, ao contrário de outras linguagens de programação, os arrays não são uma estrutura de dados embutida no Python.

## Como reverter uma lista em Python usando o método `.reverse()`:

### Usando este método Python embutido, a lista muda _no local_. Isso significa que a ordem original da lista é afetada.

### A ordem inicial dos itens é atualizada e alterada.

### Por exemplo, digamos que você tenha a seguinte lista:

```python
# Iniciar lista
my_list = [10,20,30,40,50]

print("My initial list is: ",my_list)

"""
Output:

My initial list is:  [10, 20, 30, 40, 50]
"""
```

### Para alterar os itens de `my_list` para uma ordem de `50, 40, 30, 20, 10`, você faria:

```python
# Iniciar lista
my_list = [10, 20, 30, 40, 50]

# Invertendo ordem dos itens
my_list.reverse()

print("This is what the list looks like now: ", my_list)

"""
Output:

This is what the list looks like now:  [50, 40, 30, 20, 10]
"""
```

### Você vê que a ordem inicial da lista agora mudou e os elementos dentro dela foram invertidos.

## Como reverter uma lista em Python usando o operador de fatiamento:

### O operador de fatiamento funciona de maneira semelhante à função `range()` que você viu anteriormente.

### Ele também aceita os argumentos `start`, `stop` e `step`.

### A sintaxe é semelhante a esta: `start: end: step`.

### Por exemplo:

```python
my_list = [10, 20, 30, 40, 50]

my_list2 = my_list[1:3:1]

print(my_list2)

"""
Output:

[20, 30]
"""
```

### No exemplo acima, queríamos buscar os itens começando do índice 1 até, mas não incluindo, o item com índice 3, incrementando um número por vez.

### A indexação em Python começa em 0, portanto, o primeiro elemento tem um índice de 0, o segundo elemento tem um índice de 1 e assim por diante.

### Quando você quiser imprimir todos os itens, você usa uma das seguintes maneiras:

```python
my_list = [10,20,30,40,50]

my_list2 = my_list[:]

# ou ...

my_list2 = my_list[::]

# Printar no console
print(my_list2)

"""
Output:

[10, 20, 30, 40, 50]
"""
```

### Portanto, você pode usar um ou dois dois-pontos para produzir todos os itens contidos na lista.

### Agora, para reverter todos os itens dentro da lista usando o operador de fatiamento, você deve incluir a etapa.

### Neste caso, você usa dois pontos para representar os argumentos `start` e `end`, e uma etapa negativa para decrementar:

### Nesse caso, uma nova lista é criada, com a ordem original da lista não sendo afetada.

## Como reverter uma lista em Python usando a função `reversed()`:

### Não confunda isso com o método `.reverse()`! A função `reversed()` embutida inverte a ordem de uma lista e permite que você acesse cada item individual por vez.

```python
my_list = [10,20,30,40,50]

for num in reversed(my_list): 
    print(num)
    
"""
Output:

50
40
30
20
10
"""
```

### A função `reversed()` aceita uma lista como argumento e retorna uma versão reversa iterável dos itens contidos na lista.

### Se você quiser armazenar o valor de retorno da função `reversed()` para uso posterior, deverá colocá-lo dentro do construtor `list()` e atribuir a nova lista a uma variável, assim:

## Conclusão:

### E aí está - agora você sabe o básico de como funciona a reversão de listas em Python!

### Se você quiser saber mais sobre Python, freeCodeCamp oferece uma [Certificação Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/)

### Neste currículo baseado em projeto, você começará do zero. Você aprenderá os fundamentos da programação e avançará para tópicos mais complexos.

### No final, você construirá 5 projetos para colocar suas novas habilidades em prática.

### Obrigado por ler e feliz codificação!