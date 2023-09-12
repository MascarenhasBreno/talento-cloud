def ler_ano_nascimento()-> int:
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento: "))
            if ano_nascimento < 1922 or ano_nascimento > 2021:
                raise ValueError
            return ano_nascimento
        except ValueError:
            print("Ano de nascimento inválido")

def idade_usuario(ano_atual: int)-> None:
    nome = input("Digite o nome: ")
    ano_nascimento = ler_ano_nascimento()
    idade = ano_atual - ano_nascimento
    print(f"{nome} tem {idade} anos")
    

if __name__ == '__main__':
    idade_usuario(2023)