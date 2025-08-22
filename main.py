# --- Inicialização das Variáveis ---


alturas_gerais = []
alturas_masculinas = []
numero_feminino = 0
total_de_pessoas = 15

print("--- Coleta de Dados de Altura e Gênero ---")

for i in range(total_de_pessoas):
    print(f"\n--- Inserindo dados para a {i + 1}ª pessoa ---")

    # --- Validação da Altura ---
    while True:
        try:
            altura_str = input(f"Digite a altura (em metros): ").replace(',', '.')
            altura = float(altura_str)
            if altura > 0 and altura < 3:
                break 
            else:
                print("Erro: Por favor, insira uma altura positiva e realista (ex: 1.75).")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número para a altura.")

    # --- Validação do Gênero ---
    while True:
        genero = input(f"Digite o gênero (Masculino/Feminino): ").strip().capitalize()
        if genero in ["Masculino", "Feminino"]:
            break 
        else:
            print("Erro: Gênero inválido. Por favor, digite 'Masculino' ou 'Feminino'.")

    # --- Armazenamento e Contagem dos Dados ---
    alturas_gerais.append(altura)
    if genero == "Masculino":
        alturas_masculinas.append(altura)
    else:
        numero_feminino += 1

print("\n========================================")
print("         RESULTADOS FINAIS          ")
print("========================================")

# A maior e a menor altura do grupo
if alturas_gerais:
    maior_altura = max(alturas_gerais)
    menor_altura = min(alturas_gerais)
    print(f"-> A maior altura do grupo é: {maior_altura:.2f} m.")
    print(f"-> A menor altura do grupo é: {menor_altura:.2f} m.")
else:
    print("-> Nenhum dado de altura foi inserido.")

# 2. A média de altura das pessoas do gênero Masculino
if alturas_masculinas:
    media_altura_masculina = sum(alturas_masculinas) / len(alturas_masculinas)
    print(f"-> A média de altura dos homens é: {media_altura_masculina:.2f} m.")
else:
    print("-> Nenhum homem foi inserido para calcular a média de altura.")

# 3. O número de pessoas do gênero Feminino
print(f"-> O número total de mulheres é: {numero_feminino}.")
print("========================================")