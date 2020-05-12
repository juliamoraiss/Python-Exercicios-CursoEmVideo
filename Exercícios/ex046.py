from time import sleep
import emoji
print('{:=^60}'.format(' CONTAGEM REGRESSIVA '))

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!!',(emoji.emojize(':fireworks:')*5))
