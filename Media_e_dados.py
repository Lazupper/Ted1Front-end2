# Listas e contador para armazenar os dados
alturas_geral = []
alturas_Homens = []
contador_Mulheres = 0

print("Media e dados de 15 pessoas")

# Loop para perguntar 15 vezes
for i in range(15):
    print(f"\nPessoa {i + 1}")

    # Coleta a altura e o gênero sem validação
    altura = float(input(" diga o tamanho em  metros (ex: 1.80): "))
    genero = input(" gênero (H/M): ").upper()

    # Adiciona a altura na lista geral
    alturas_geral.append(altura)

    # Verifica o gênero para adicionar nas listas específicas
    if genero == 'H':
        alturas_Homens.append(altura)
    elif genero == 'M':
        contador_Mulheres += 1

# --- Exibição dos resultados ---
print("Olha a Situação")

# Maior e menor altura
print(f"Maior altura do grupo: {max(alturas_geral):.2f}m")
print(f"Menor altura do grupo: {min(alturas_geral):.2f}m")

# Média de altura dos homens
if alturas_Homens:
    media_Homens = alturas_Homens / alturas_Homens
    print(f"Média de altura dos Homens: {media_homens:.2f}m")
else:
    print("Nenhuma altura de Homens foi registrada.")

# Número de mulheres
print(f"Número de Mulheres: {contador_Mulheres}")
