import requests
import time
import json
import os


class TelegramBot:
    def __init__(self):
        token = '1593336405:AAHP2CkoPUePWj3-Lp1sjRWS1rsFto24Brg'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('inicio', 'Inicio'):
            return f'''Olá bem vindo(a) a @_Desapega_, como posso te ajudar?:{os.linesep}1 - Comprar uma peça de roupa.{os.linesep}2 - Falar com a Larissa ou Sthefany.{os.linesep}3 - Alguma duvida em relação a loja ou outro assunto.'''
        if mensagem == '1':
            return f'''Já segue nosso insta?{os.linesep}(s/n)
            '''
        elif mensagem == '2':
            return f'''Já segue nosso insta?{os.linesep}(s/n)
            '''
        elif mensagem == '3':
            return f'''Já segue nosso insta?{os.linesep}(s/n)'''

        elif mensagem.lower() in ('s', 'sim'):
            return ''' Que ótimo, já já entraremos em contato com você... Muito obrigada <3!!! '''
        elif mensagem.lower() in ('n', 'não'):
            return ''' Não perca nossas novidades e postagens, segue lá <3!!! Já Já entraremos em contato com você... Muito obrigada <3!!! '''
        else:
            return 'Gostaria de mandar outra mensagem? Digite "inicio"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()