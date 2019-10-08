x = input('Digite algo: ')
print('O tipo primitivo desse valor é {}\n'
      'Só tem espaços? {}\n'
      'É maiúscula? {}\n'
      'É minúsculo? {}\n'
      .format(type(x),x.isspace(),x.isupper(),x.islower()))

