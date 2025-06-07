# Funções de conversão, utilizam fórmulas aritméticas
# básicas para multiplicar, ou dividir pelo valor atribuído.
def metros_para_km(metros):
    return metros / 1000

def km_para_metros(km):
    return km * 1000

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kg_para_gramas(kg):
    return kg * 1000

def gramas_para_kg(gramas):
    return gramas / 1000

def kg_para_libras(kg):
    return kg * 2.20462

def libras_para_kg(libras):
    return libras / 2.20462

def metros_para_pes(metros):
    return metros * 3.28084

def pes_para_metros(pes):
    return pes / 3.28084

# Função responsável por exibir o menu.
def menu():
    print("Conversor de Medidas")
    print("1. Metros para Quilômetros")
    print("2. Quilômetros para Metros")
    print("3. Celsius para Fahrenheit")
    print("4. Fahrenheit para Celsius")
    print("5. Quilos para Gramas")
    print("6. Gramas para Quilos")
    print("7. Quilos para Libras (kg -> lb)")
    print("8. Libras para Quilos (lb -> kg)")
    print("9. Metros para Pés (m -> ft)")
    print("10. Pés para Metros (ft -> m)")

# Loop principal, que imprime a escolha do usuário.
while True:
    menu()
    escolha = input("Escolha uma das opções na lista: ").strip()

    if escolha == "":
        print("Saindo do programa...")
        break
    try:
        valor_str = input("Digite o valor, ou tecle Enter para voltar ao menu: ").strip()
        if valor_str == "":
            continue
        valor = float(valor_str)

        if escolha == "1":
            print(f"{valor} metros = {metros_para_km(valor)} km")
            break
        elif escolha == "2":
            print(f"{valor} km = {km_para_metros(valor)} metros")
            break
        elif escolha == "3":
            print(f"{valor} °C = {celsius_para_fahrenheit(valor)} °F")
            break
        elif escolha == "4":
            print(f"{valor} °F = {fahrenheit_para_celsius(valor)} °C")
            break
        elif escolha == "5":
            print(f"{valor} kg = {kg_para_gramas(valor)} g")
            break
        elif escolha == "6":
            print(f"{valor} g = {gramas_para_kg(valor)} kg")
            break
        elif escolha == "7":
            print(f"{valor} kg = {kg_para_libras(valor):.2f} lb")
            break
        elif escolha == "8":
            print(f"{valor} lb = {libras_para_kg(valor):.2f} kg")
            break
        elif escolha == "9":
            print(f"{valor} m = {metros_para_pes(valor):.2f} ft")
            break
        elif escolha == "10":
            print(f"{valor} ft = {pes_para_metros(valor):.2f} m")
            break

    # Tratamento diverso para erros, esperados ou inesperados.
        else:
            print("Opção inválida.")
    except ValueError:
        print("Por favor, digite um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    print()
