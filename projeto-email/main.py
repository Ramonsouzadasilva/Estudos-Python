import re

import mandar_email

padrao_email = '\w{2,50}@\w{2,15}\.[a-z]{2,3}'
while True:
    destinatario = input(str('Informe o email que deseja enviar o relatório: '))
    e_email = re.findall(padrao_email, destinatario)
    if not e_email:
        print(f'Email inválido!!\nPor favor insira um email válido [teste@exemplo.com]')
    else:
        break

mandar_email.enviar_email(destinatario)
