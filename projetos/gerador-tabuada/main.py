# Importa o módulo de tempo, usado para adicionar pequena
# pausa nas interações mais à frente no código.
import time

def exibir_tabuada(numero):
    print(f"\n{'*' * 20}")
    print(f"Tabuada do {numero}:".center(20))
    print(f"{'*' * 20}\n")
    
    # Exibindo a tabuada do número escolhido, vai de 0 a 10.
    for i in range(11):
        print(f"{numero} x {i} = {numero * i}")

    print("\n" + "*" * 20)

# Cria o menu do programa e detecta a entrada do usuário,
# de um número de 1 a 1000.
def main():
    while True:
        try:
            print("\nGerador de tábuadas, seja bem-vindo!")
            numero = input("Digite um número de 0 a 1000 para gerar a tabuada (ou tecle Enter para sair): ")
            
            # Se o usuário apertar Enter sem digitar nada, o programa encerra.
            if numero == "":
                print("\nEncerrando... Até logo! 👋")
                break

            # Verifica se a entrada é um número. Caso não seja, trata o erro.
            if numero.isdigit():
                numero = int(numero)
                if 0 <= numero <= 1000:
                    exibir_tabuada(numero)
                else:
                    print("\n⚠️ Por favor, digite um número entre 0 e 1000.")
            else:
                print("\n⚠️ Entrada inválida. Por favor, digite um número.")
            
            time.sleep(1)

        # Tratamento genérico para erro inesperado.
        except Exception as e:
            print(f"\n Ocorreu um erro inesperado: {e}")
            print("Por favor, tente novamente.\n")
            time.sleep(1)

if __name__ == "__main__":
    main()
