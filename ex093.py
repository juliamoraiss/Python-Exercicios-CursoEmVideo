jogador = dict()
jogador['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
listagols = list()
for p in range(1, partidas + 1):
    gols = int(input(f'Quantos gols na partida {p}? '))
    listagols.append(gols)
jogador['Gols'] = listagols[:]
jogador['Total'] = sum(listagols)
print('-='*25)
print(jogador)
print('-='*25)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*25)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'   => Na partida {c + 1} fez {jogador["Gols"][c]} gol(s) ')
print(f'Foi um total de {sum(listagols)} gol(s)')