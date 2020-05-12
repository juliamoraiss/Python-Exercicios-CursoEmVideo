import requests

try:
    url = 'http://pudim.com.br/'
    response = requests.get(url)
    print(f'\n\33[32m{" CONEXÃO REALIZADA COM SUCESSO ":-^43}')
    print('É possível acessar o site no momento.'.center(43))
    print(f'URL: {url}'.center(43))
    print('-' * 43 + '\33[m')

except:
    print(f'\n\33[31m{" ERRO ":-^41}')
    print(f'Não é possível acessar o site no momento.\n{"Tente novamente!".center(41)}')
    print('-' * 41 + '\33[m')
