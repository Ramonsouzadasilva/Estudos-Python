import yagmail
import json


def enviar_email(destinatario):
    with open("informacao_email.json", "r") as arquivo:
        conteudo_arquivo = json.load(arquivo)
        email = conteudo_arquivo['email']
        senha = conteudo_arquivo['senha']

    usuario = yagmail.SMTP(user=email, password=senha)

    usuario.send(
        to=destinatario,
        subject='Planilha',
        contents='Em anexo, segue a planilha de excel com os dados.',
        attachments='Planilha de Produtos.xlsx')

    print('\nEMAIL ENVIADO !!!!\n')
