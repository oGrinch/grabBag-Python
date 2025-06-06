# Função que realiza o cálculo da expressão informada
def calcular(expressao):
    try:
        # Verifica se o usuário tentou usar '=' na expressão
        if "=" in expressao:
            raise ValueError("Erro: O sinal de igual (=) não é válido nessa posição.")
        
        # Usa eval() para avaliar a expressão matemática
        resultado = eval(expressao)
        return resultado

    # Trata possível erro causado por divisão por zero (0)
    except ZeroDivisionError:
        return "Erro! Divisão por zero."
    
    # Trata o erro causado por uso do '='
    except ValueError as ve:
        return str(ve)
    
    # Trata qualquer outro erro inesperado
    except Exception as e:
        return f"Erro: Expressão inválida. {e}"

# Define função para que haja um menu simples para interação com o usuário
def menu():
    print("Bem-vindo à Calculadora!")
    print("Escolha uma operação e digite seu respectivo sinal:\n' + ' para soma, \n' - ' subtração, \n' * ' multiplicação, \n' / ' divisão.")
    print("Escreva no formato: a + b.")
    print("Para encerrar, aperte apenas 'enter'.")

    # Loop principal, funciona até o usuário digitar algo
    while True:
        expressao = input("\nDigite a operação: ")
        
        # Encerra o programa se apenas a tecla enter for apertada
        if expressao.lower() == '':
            print("Até logo! Encerrando...")
            break
        
        # Chama a função para calcular, exibe o resultado
        resultado = calcular(expressao)
        print(f"= {resultado}")

# Chama o menu se o script for executado diretamente
if __name__ == "__main__":
    menu()
