# Importando os módulos padrão "string" e "random".
# string tem alguns conjuntos predefinidos de caracteres
# diversos, e o random serve para gerar a miscelânea.

# Nota: sequências aleatórias geradas em código ainda são
# "previsíveis" de certa forma. Enquanto não é um problema
# para fins educacionais e pessoais, é bom manter isso em
# mente para tarefas que exigem maior segurança.
import string
import random

# Define a função principal (gerar senhas) e o máximo de 
# caracteres. A seguir, tratamento de erro, em caso o usuário:
# digite 0; digite um número negativo; digite um número maior
# do que o máximo de caracteres permitidos; digite uma letra ou
# algum outro caractere. Inclui também tratamento para erros 
# inesperados de qualquer espécie.
def gerar_senha():
    MAX_CARACTERES = 60
    
    while True:
        try:
            tamanho = int(input(f"Seja bem-vindo! Siga as instruções para que possa receber uma senha forte, compilando caracteres aleatórios! Apenas para fins educacionais.\n \n Quantos caracteres deseja para sua senha? (máximo de 60): "))
            if tamanho <= 0:
                print("O valor digitado deve ser entre 1 e 60.\n")
            elif tamanho > MAX_CARACTERES:
                print(f"O tamanho máximo permitido é de {MAX_CARACTERES} caracteres.\n")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

# Sequencialmente, após pedir o número de caracteres, permite que o
# usuário solicite, digitando s (sim) ou n (não): letras maiúsculas;
# letras minúsculas; números e/ou caracteres especiais.
    while True:
        incluir_maiusculas = input("Deseja incluir letras maiúsculas? (s/n): ").lower()
        if incluir_maiusculas not in ['s', 'n']:
            print("Por favor, responda 's' para sim ou 'n' para não.")
        else:
            incluir_maiusculas = incluir_maiusculas == 's'
            break
    while True:
        incluir_minusculas = input("Deseja incluir letras minúsculas? (s/n): ").lower()
        if incluir_minusculas not in ['s', 'n']:
            print("Por favor, responda 's' para sim ou 'n' para não.")
        else:
            incluir_minusculas = incluir_minusculas == 's'
            break
    while True:
        incluir_numeros = input("Deseja incluir números? (s/n): ").lower()
        if incluir_numeros not in ['s', 'n']:
            print("Por favor, responda 's' para sim ou 'n' para não.")
        else:
            incluir_numeros = incluir_numeros == 's'
            break
    while True:
        incluir_sinais = input("Deseja incluir caracteres especiais? (s/n): ").lower()
        if incluir_sinais not in ['s', 'n']:
            print("Por favor, responda 's' para sim ou 'n' para não.")
        else:
            incluir_sinais = incluir_sinais == 's'
            break

# Irá definir os caracteres a serem usados e "impressos".
    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_sinais:
        caracteres += string.punctuation

# Tratamento de erro que verifica se o usuário escolheu 
# algum tipo de caractere. 
    if not caracteres:
        print("Você deve selecionar pelo menos um tipo de caractere!")
        return

# Gera a senha aleatória em questão.
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Inprime a senha gerada no console.
senha_gerada = gerar_senha()
if senha_gerada:
    print(f"Sua senha gerada: {senha_gerada}")
