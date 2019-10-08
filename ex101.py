def voto(n):
    from datetime import datetime
    idade = datetime.today().year - n
    print(f'Com {idade} anos: ', end='')
    if 16 <= idade < 18 or idade > 65:
        return "VOTO OPCIONAL"
    elif idade >= 18:
        return "VOTO OBRIGATÓRIO"
    elif idade < 16:
        return "NÃO VOTA"


print('-'*28)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))