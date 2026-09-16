import random


def analise_valor_limite(valor_min, valor_max):
    print("\n--- Análise de Valor-Limite ---")

    valores = [
        valor_min - 1,
        valor_min,
        valor_min + 1,
        valor_max - 1,
        valor_max,
        valor_max + 1
    ]

    for valor in valores:
        if valor < valor_min:
            classificacao = "Inválido - abaixo do mínimo"
        elif valor > valor_max:
            classificacao = "Inválido - acima do máximo"
        else:
            classificacao = "Válido"

        print(f"Valor: {valor} -> {classificacao}")


def particionamento_classes(valor_min, valor_max):
    print("\n--- Particionamento em Classes de Equivalência ---")

    # Classe inválida: abaixo do valor mínimo
    valor_inferior = random.randint(valor_min - 100, valor_min - 1)

    print("\nClasse 1: Valores menores que o mínimo")
    print(f"Valor sorteado: {valor_inferior}")
    print("Resultado: Inválido")

    # Classe válida: dentro da faixa
    valor_valido = random.randint(valor_min, valor_max)

    print("\nClasse 2: Valores dentro da faixa")
    print(f"Valor sorteado: {valor_valido}")
    print("Resultado: Válido")

    # Classe inválida: acima do valor máximo
    valor_superior = random.randint(valor_max + 1, valor_max + 100)

    print("\nClasse 3: Valores maiores que o máximo")
    print(f"Valor sorteado: {valor_superior}")
    print("Resultado: Inválido")


def main():
    print("=== ANÁLISE DE TESTES ===")

    print("\nEscolha o critério:")
    print("1 - Análise de Valor-Limite")
    print("2 - Particionamento em Classes de Equivalência")
    print("3 - Ambos")

    criterio = input("\nDigite sua opção: ")

    valor_min = int(input("Digite o valor mínimo: "))
    valor_max = int(input("Digite o valor máximo: "))

    if valor_min >= valor_max:
        print("Erro: o valor mínimo deve ser menor que o valor máximo.")
        return

    if criterio == "1":
        analise_valor_limite(valor_min, valor_max)

    elif criterio == "2":
        particionamento_classes(valor_min, valor_max)

    elif criterio == "3":
        analise_valor_limite(valor_min, valor_max)
        particionamento_classes(valor_min, valor_max)

    else:
        print("Opção inválida.")


main()
