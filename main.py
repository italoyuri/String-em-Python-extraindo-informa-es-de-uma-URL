url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

if __name__ == "__main__":
    # Em que pese o instrutor ter ensinado através do [], preferi fazer da forma como eu já sabia

    partials = url.split("?")
    parametros = partials[1].split("&")

    print(f"Primeiro fatiamento: {partials}\n")
    print(f"Segundo fatiamento: {parametros}\n")
