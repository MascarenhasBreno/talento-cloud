def soma(a: float, b: float) -> float:
    return a + b

def subtracao(a: float, b: float) -> float:
    return a - b

def divisao(a: float, b: float) -> float:
    try:
        return a / b
    except:
        raise ZeroDivisionError('Não é possível dividir por zero')
    
def multiplicacao(a: float, b: float) -> float:
    return a * b

def calculadora(operador:str, a: float, b:float) -> float:
    if operador == '+':
        return soma(a, b)
    elif operador == '-':
        return subtracao(a, b)
    elif operador == '/':
        return divisao(a, b)
    elif operador == '*':
        return multiplicacao(a, b)
    else:
        return 0


if __name__ == '__main__':
    try:
        print(calculadora("/", 2, 5))
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
