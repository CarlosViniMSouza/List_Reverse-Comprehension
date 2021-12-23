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

## O que é compreensão de lista em Python? Uma visão geral da sintaxe:

### Ao analisar e trabalhar com listas em Python, muitas vezes você terá que manipular, modificar ou realizar cálculos em cada item da lista, de uma só vez.

### Você também pode precisar criar novas listas do zero ou criar uma nova lista com base nos valores de uma lista já existente.

### A compreensão de listas é uma maneira rápida, curta e elegante de criar listas em comparação com outros métodos iterativos, como loops `for`.

### A sintaxe geral para compreensão de lista é assim:

```
new_list = [expression for variable in iterable]
```

### Vamos decompô-lo:

### ° As compreensões de listas começam e terminam com colchetes de abertura e fechamento, `[]`.

### ° Em seguida, vem a `expression` ou operação que você gostaria de realizar e realizar em cada valor dentro do iterável atual. Os resultados desses cálculos entram na nova lista.

### ° A `expression` é seguida por uma cláusula `for`.

### ° `variable` é um nome temporário que você deseja usar para cada item da lista atual que está passando pela iteração.

### ° A palavra-chave `in` é usada para fazer um loop no iterável.

### ° `iterable` pode ser qualquer objeto Python, como uma lista, tupla, string e assim por diante.

### ° A partir da iteração que foi realizada e os cálculos que ocorreram em cada item durante a iteração, novos valores foram criados, os quais são salvos em uma variável, neste caso `new_list`. *A lista antiga (ou outro objeto) permanecerá inalterada*.

### ° Pode haver uma instrução `if` opcional e uma cláusula `for` adicional.

## Como usar a compreensão de lista em Python:

### Usando o mesmo exemplo anterior, aqui está como você criaria uma nova lista de números de 0 a 4 com a função `range()` em apenas uma linha, usando a compreensão de lista:

```python
# Topico -> Como usar a compreensão de lista em Python:
new_list = [num for num in range(5)]

print(new_list)

"""
Output:

[0, 1, 2, 3, 4]
"""
```

### Isso tem a mesma saída que o exemplo do loop for, mas com significativamente menos código!

### Vamos decompô-lo:

### ° o iterável, neste caso, é uma sequência de números de 0 a 4, usando o `range(5)`. `range()` constrói uma lista de números.

### ° Você usa a palavra-chave `in` para iterar os números.

### ° O `num` após a cláusula `for` é uma variável, um nome temporário para cada valor no iterável. Então, `num` seria igual a `0` na primeira iteração, então `num` seria igual a `1` na próxima iteração e assim por diante, até atingir e igualar o número 4, onde a iteração pararia.

### ° O `num` antes da cláusula `for` é uma expressão para cada item na sequência.

### ° Finalmente, a nova lista (ou outro iterável) que é criada é armazenada na variável `new_list`.

### Você pode até realizar operações matemáticas nos itens contidos no iterável e o resultado será adicionado à nova lista:

```python
new_list = [num * 2 for num in range(5)]

print(new_list)

"""
Output:

[0, 2, 4, 6, 8]
"""
```

### Aqui, cada número no `range(5)` será multiplicado por dois e o novo valor será armazenado na variável `new_list`.

### E se você tivesse uma lista pré-existente onde deseja manipular e modificar cada item? Isso seria semelhante ao exemplo anterior, onde criamos uma lista de quadrados.

### Novamente, você pode conseguir isso com apenas uma linha de código, usando a compreensão de lista:

## Como usar condicionais com compreensão de lista em Python:

### Opcionalmente, você pode usar uma instrução `if` com uma compreensão de lista.

### A sintaxe geral é semelhante a esta:

```
new_list = [expression for variable in iterable if condition == True]
```

### As condicionais atuam como um filtro e adicionam uma verificação extra para precisão e personalização adicionais ao criar uma nova lista.

### Isso significa que o valor na expressão deve atender a certos critérios e a uma determinada condição especificada por você, para poder entrar na nova lista.

```python
new_list = [num for num in range(50) if num % 2 == 0]

print(new_list)

"""
Output:

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
"""
```

### No exemplo acima, apenas os valores onde a condição `num% 2 == 0` é verificada e avalia como True entrarão em `new_list`.

### O operador módulo é usado em cada um dos números na sequência de números começando em 0 e terminando em 49.

### Se o restante dos números quando dividido por 2 for 0, então e somente então ele entra na lista.

### Portanto, neste caso, ele cria uma lista apenas com números pares.

### Você pode então torná-lo tão específico quanto desejar.

### Por exemplo, você pode adicionar mais de uma condição, assim:

```python
new_list = [num for num in range(50) if  num > 20 and num % 2 == 0]

print(new_list)

"""
Output:

[22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
"""
```

### Neste exemplo, existem duas condições `num > 20` e `num % 2 == 0`.

### O operador `and` indica que ambos devem ser atendidos para que o valor seja adicionado à nova lista.

### Os valores que não atendem às condições são excluídos e não são adicionados.

## Como usar a compreensão de lista em strings em Python:

### Você pode criar uma nova lista com os caracteres individuais contidos em uma determinada string.

```python
fave_language_chars = [letter for letter in "Python"]

print(fave_language_chars)

"""
Output:

['P', 'y', 't', 'h', 'o', 'n']
"""
```

### A nova lista criada é composta por todas as letras separadas contidas na string "Python", que atua como um iterável.

### Assim como os números, você pode realizar operações nos caracteres contidos em uma string e personalizá-los, dependendo de como deseja que eles estejam na nova lista criada.

### Se você quiser que todas as letras sejam maiúsculas, você faria o seguinte:

```python
fave_language_chars_upper = [letter.upper() for letter in "Python"]

print(fave_language_chars_upper)

"""
Output:

['P', 'Y', 'T', 'H', 'O', 'N']
"""
```

### Aqui, você usa o método `.upper()` para converter todas as letras em "Python" em maiúsculas e adicioná-las à variável `fave_language_chars_upper`.

### O mesmo acontece se você quiser que todas as letras sejam minúsculas - em vez disso, use o método `lower()`.


## Conclusão:

### E aí está! Agora você conhece os fundamentos da compreensão de listas em Python.

### Ele oferece uma sintaxe elegante e concisa para a criação de novas listas com base em listas existentes ou outros iteráveis.

### Se você estiver interessado em aprender mais sobre Python, freeCodeCamp tem uma [Certificação Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

## Neste currículo baseado em projeto, você começará aprendendo os fundamentos da programação e avançará para assuntos mais complexos, como estruturas de dados. Você também construirá cinco projetos para colocar em prática o que aprendeu.

### Obrigado por ler e feliz codificação!