'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''

# Quebrando o problema:

# Função para calculo da fibonacci e verificação
def fibonacci(num):
    # definindo as variáveis necessárias.
    fib_anterior = 0
    fib_atual = 1
    # loop que realizará o andar da sequência de Fibonacci até que a variável fib_atual seja menor que num.
    while fib_atual < num:
        fib_prox = fib_anterior + fib_atual
        fib_anterior = fib_atual
        fib_atual = fib_prox
    # informando se o valor inserido pertence ou não a Fibonacci.
    if fib_atual == num:
        print(f"{num} pertence à sequência de Fibonacci.")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")
    return fib_anterior

# Solicitando a entrada do usuário
while True:
    try:
        num = int(input("Digite um número: "))
        break
    except ValueError:
        print("O caractere digitado não é valido, digite um número.")

fibonacci(num)
