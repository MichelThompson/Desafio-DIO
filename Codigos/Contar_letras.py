def contar_letras(texto):
    """
    Conta a frequência de cada letra em um texto.

    Parâmetros:
    texto (str): O texto onde as letras serão contadas.

    Retorna:
    dict: Um dicionário com as letras como chaves e suas frequências como valores.
    """
    # Inicializa um dicionário vazio para armazenar as contagens
    contagem = {}

    # Percorre cada caractere no texto
    for letra in texto:
        # Converte o caractere para minúsculo para uma contagem case-insensitive
        letra = letra.lower()
        # Verifica se o caractere é uma letra
        if letra.isalpha():
            # Incrementa a contagem da letra no dicionário
            if letra in contagem:
                contagem[letra] += 1
            else:
                contagem[letra] = 1

    return contagem

# Exemplo de uso:
texto = "Exemplo de texto para contagem de letras."
contagem_letras = contar_letras(texto)
print("Contagem de letras:")
for letra, contagem in contagem_letras.items():
    print(f"{letra}: {contagem}")
