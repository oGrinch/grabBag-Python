# Importando o módulo time para uso posterior.
import time

def calcular(expressao): # Define a expressão 'calcular'.
    try:
        # Verifica se o sinal de igual (=) foi usado pelo usuário na expressão.

        # Também atua como validação básica para evitar que o usuário tente atribuir
        # algo, vide o uso da função eval().
        if "=" in expressao:
            raise ValueError("Erro: O sinal de igual (=) não é válido nessa posição.")

        # Utiliza a função 'eval()' embutida para validar a expressão.

        # ATENÇÃO: eval() pode ser usada para inputs maliciosos. Enquanto
        # usável para fins acadêmicos e aprendizado, não deve-se usar
        # junto com entradas não confiáveis.
        resultado = eval(expressao)
        return resultado

    # Trata do erro específico caso o usuário tente dividir por zero.
    except ZeroDivisionError:
        return "Erro! Divisão por zero."
    except ValueError as ve:
        return str(ve) # Trata erros de valor e retorna a mensagem.

    # Trata outros erros não previstos no código.
    except Exception as e:
        return f"Erro: Expressão inválida. {e}"

# Define e exibe o menu, gerenciando o loop de entrada do usuário.
def menu():
    print("Bem-vindo à Calculadora!")
    print("Escolha uma operação e digite seu respectivo sinal:\n' + ' para soma, \n' - ' subtração, \n' * ' multiplicação, \n' / ' divisão.")
    print("Escreva no formato: a + b.")
    print("Para encerrar, aperte apenas 'enter'.")

# Abre o loop para que o usuário possa fazer sua solicitação.
    while True:
        expressao = input("\nDigite a operação: ")
 
       # Encerra o código caso o usuário aperte a tecla 'enter',
       # ou seja, deixou a string vazia.
        if expressao.lower() == '':
            print("Até logo! Encerrando...")
            break

      # Chama a função 'calcular' para processar a expressão
      # que foi digitada pelo usuário, e exibe o resultado.
        resultado = calcular(expressao)
        print(f"= {resultado}")

    # Adiciona 1 segundo de delay entre as interações, para
    # melhor leitura do usuário.
    time.sleep(1)

# Chama a função 'menu", inciando a calculadora.

# A função menu será chamada apenas se o arquivo principal,
# ou main, for executado.
if __name__ == "__main__":
    menu()
