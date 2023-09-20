from calculadora import calculadora as calc # Importa a função calculadora do arquivo calculadora.py

def mostrar_opcoes()-> None:
    print("Escolha uma das opções abaixo:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    
def ler_numeros() -> tuple:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return (a, b)

def menu_calculadora() -> None:
    while True:
        mostrar_opcoes()
        opcao = input("Opção: ")
        if opcao == '0':
            print("Até logo!")
            return
        elif opcao == '1':
            operador = '+'
        elif opcao == '2':
            operador = '-'
        elif opcao == '3':
            operador = '*'
        elif opcao == '4':
            operador = '/'
        else:
            print("Essa opção não existe")
            continue
        a, b = ler_numeros()
        try:
            print(f"Resultado: {calc(operador, a, b)}")
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

if __name__ == '__main__':
    menu_calculadora()
