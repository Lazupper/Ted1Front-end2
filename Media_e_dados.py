# Listas e contador para armazenar os dados
alturas_geral = []
alturas_Homens = []
contador_Mulheres = 0

print("Media e dados de 15 pessoas")

# Loop para perguntar 15 vezes
for i in range(1, 16):
    print(f"\nPessoa {i}:")

    # Coleta a altura e o gênero sem validação
    altura = float(input(" diga o tamanho em  metros (ex: 1,80): "))
    genero = input(" gênero (H/M): ").upper()

    # Adiciona a altura na lista geral
    alturas_geral.append(altura)

    # Verifica o gênero para adicionar nas listas específicas
    if genero == 'H':
        alturas_masculino.append(altura)
    elif genero == 'M':
        contador_feminino += 1

# --- Exibição dos resultados ---
print("\n--- Resultados ---")

# Maior e menor altura
print(f"Maior altura do grupo: {max(alturas_geral):.2f}m")
print(f"Menor altura do grupo: {min(alturas_geral):.2f}m")

# Média de altura dos homens
if alturas_masculino:
    media_masculino = sum(alturas_masculino) / len(alturas_masculino)
    print(f"Média de altura do gênero Masculino: {media_masculino:.2f}m")
else:
    print("Nenhuma altura de gênero masculino foi registrada.")

# Número de mulheres
print(f"Número de pessoas do gênero Feminino: {contador_feminino}")