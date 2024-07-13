def calcular_porcentagem(total, porcentagem):
    """
    Calcula a porcentagem de um valor total.

    Parâmetros:
    total (float): O valor total.
    porcentagem (float): A porcentagem a ser calculada.

    Retorna:
    float: O valor correspondente à porcentagem do total.
    """
    return (total * porcentagem) / 100

# Exemplos de uso:
valor_total = 200  # valor total
porcentagem = 15   # porcentagem a ser calculada

resultado = calcular_porcentagem(valor_total, porcentagem)
print(f"{porcentagem}% de {valor_total} é {resultado}")
