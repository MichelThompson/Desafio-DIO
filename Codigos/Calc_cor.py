import random

def gerar_cor_hexadecimal():
    """
    Gera um código de cor hexadecimal aleatório.

    Retorna:
    str: O código de cor hexadecimal.
    """
    letras_numeros = '0123456789ABCDEF'
    cor = '#'
    for _ in range(6):
        cor += random.choice(letras_numeros)
    return cor

# Exemplo de uso:
codigo_cor = gerar_cor_hexadecimal()
print(f"O código de cor gerado é: {codigo_cor}")
