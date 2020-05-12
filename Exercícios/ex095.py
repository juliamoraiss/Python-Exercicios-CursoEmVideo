jogador = dict()
listagols = list()
listajogadores = list()
somagols = 0
while True:
    jogador.clear()
    listagols.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for p in range(1, partidas + 1):
        gols = int(input(f'Quantos gols na partida {p}? '))
        somagols += gols
        listagols.append(gols)
    jogador['Gols'] = listagols[:]
    jogador['Total'] = somagols
    listajogadores.append(jogador.copy())
    opcao = str(input('Quer continuar: [S/N] ')).upper()
    if opcao == 'N':
        break

while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    print(f'-- LEVANTAMENTO DO JOGADOR {listajogadores[dados]["Nome"]}')
    for i, g in enumerate(listagols):
        print(f'No jogo {i + 1} fez {g} gol(s)')
    if dados == 999:
        break
