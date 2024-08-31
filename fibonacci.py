fib = int(input('Input para a sequência: '))

def fibonacci(num):
    a = 0
    b = 1
    lista = [a]
    lista.append(b)
    for i in range(num):
        if (b > num):
            break
        calc = a + b
        a = b
        b = calc
        if(num >= calc):
            lista.append(b)

    if(num in lista or num == 0):
        print(f'{num} pertence a sequência de Fibonacci')
    else:
        print(f'{num} não pertence a sequência de Fibonacci')

    print(lista)

fibonacci(fib)