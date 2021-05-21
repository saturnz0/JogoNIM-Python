
def ModoDeJogo():
    modoDeJogoSelecionado = 0
    modosDeJogo = ["Partida Isolada", "Campeonato"]


    print("Bem-vindo ao jogo do NIM! Selecione um modo de jogo:\n")
    for chave, modo in enumerate(modosDeJogo):
        print("{} - {}".format(chave + 1, modo))


    while modoDeJogoSelecionado > len(modosDeJogo) or modoDeJogoSelecionado < 1:
        modoDeJogoSelecionado = int(input("Qual modo você deseja jogar? "))

    print("Você selecionou o modo: {}\n".format(modosDeJogo[modoDeJogoSelecionado - 1]))

    return modoDeJogoSelecionado

def computador_escolhe_jogada(n, m):
    pecasRestantesNoJogo = n
    limitePecasRemovidas = m
    escolhaDoComputador = 0

    if pecasRestantesNoJogo <= limitePecasRemovidas:
        escolhaDoComputador = pecasRestantesNoJogo
    else:
        for i in range(1, (limitePecasRemovidas + 1)):
            if (pecasRestantesNoJogo - i) % (limitePecasRemovidas + 1) == 0:
                escolhaDoComputador = i

    
    if escolhaDoComputador == 0:
        escolhaDoComputador = limitePecasRemovidas

    return escolhaDoComputador

def usuario_escolhe_jogada(n, m):
    pecasRestantesNoJogo = n
    limitePecasRemovidas = m
    escolhaDoJogador = 0

    if pecasRestantesNoJogo >= limitePecasRemovidas:
        limitePecasRemovidasNaJogada = limitePecasRemovidas
    else:
        limitePecasRemovidasNaJogada = pecasRestantesNoJogo

    while escolhaDoJogador > limitePecasRemovidasNaJogada or escolhaDoJogador < 1:
        escolhaDoJogador = int(input("Quantas peças você vai tirar? "))

    return escolhaDoJogador

def partida():
    computadorVenceu = True
    turnoDoComputador = False
    limitePecasPorJogada = 0


    totalDePecas = int(input("Quantas peças? "))

    while limitePecasPorJogada < 1:
        limitePecasPorJogada = int(input("Limite de peças por jogada? "))
    if totalDePecas % (limitePecasPorJogada + 1) == 0:
        print("Você começa!\n")
        turnoDoComputador = False
    else:
        print("Computador começa!\n")
        turnoDoComputador = True


    while totalDePecas > 0:
        if turnoDoComputador:
            pecasRetiradas = computador_escolhe_jogada(totalDePecas, limitePecasPorJogada)
            print("O computador tirou {} peca(s).".format(pecasRetiradas))
        else:
            pecasRetiradas = usuario_escolhe_jogada(totalDePecas, limitePecasPorJogada)
            print("Você tirou {} peca(s).".format(pecasRetiradas))

    
        totalDePecas = totalDePecas - pecasRetiradas

        
        if totalDePecas > 1:
            print("Agora restam {} peças no tabuleiro.\n".format(totalDePecas))
        elif totalDePecas == 1:
            print("Agora resta apenas uma peça no tabuleiro.")

        turnoDoComputador = not turnoDoComputador

    
    if not turnoDoComputador:
        print("O computador ganhou!")
    else:
        computadorVenceu = False
        print("Você ganhou!")

    return(computadorVenceu)


def campeonato():
    numeroDaRodada = 1
    pontosDoComputador = 0
    pontosDoUsuario = 0

    
    while numeroDaRodada < 4:
        print("**** Rodada {} ****\n".format(numeroDaRodada))

        
        if partida():
            pontosDoComputador += 1
        else:
            pontosDoUsuario += 1

        
        numeroDaRodada += 1

    
    print("Placar: Você {} X {} Computador".format(pontosDoUsuario, pontosDoComputador))


def main():
    modoDeJogo = ModoDeJogo()
    partida() if modoDeJogo == 1 else campeonato()

main()
