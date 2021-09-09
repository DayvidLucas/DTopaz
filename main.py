from helper import ServidorHelper


def carrega_dados(arquivo_entrada, arquivo_saida) -> None:
    arquivo = open(arquivo_entrada, "r")
    arquivo_saida = open(arquivo_saida, "w")
    entradas = []
    index: int = 0
    umax: int = 0
    ttasks: int = 0

    for linha in arquivo:
        if index == 0:
            ttasks = int(linha)

        elif index == 1:
            umax = int(linha)
        else:
            entradas.append(int(linha.strip()))
        index += 1
    arquivo.close()

    response = valida_entrada(ttasks, umax, entradas)
    if response == "EXECUTA":
        executa_ciclo(entradas, ttasks, umax, arquivo_saida)
    else:
        print(response)


def executa_ciclo(entradas: int, ttasks: int, umax: int, arquivo_saida) -> None:
    helper = ServidorHelper(ttasks)
    helper.valida_servidor_vazio(entradas, umax, arquivo_saida)
    arquivo_saida.close()


def valida_entrada(ttasks, umax, entradas) -> str:
    if not 1 <= umax <= 10:
        return f"Maximo de Usuario deve estar entre 1 e 10 -> Valor: {umax}"
    elif not 1 <= ttasks <= 10:
        return f"Maximo de ttask deve estar entre 1 e 10 -> Valor: {ttasks}"
    elif len(entradas) == 0:
        return f"Arquivo sem nenhuma entrada:"
    else:
        return 'EXECUTA'


if __name__ == "__main__":
    carrega_dados("input.txt", "output.txt")
