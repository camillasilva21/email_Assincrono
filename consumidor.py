import stomp
import json

class Email_Consumer(stomp.ConnectionListener):

    def on_message(self, message):
        print('Novo pedido de envio de e-mail recebido:\n\n', message.body)
        self.process_email(message.body)

    def process_email(self, message):
        data_email = json.loads(message)
        user_email = data_email['destinatario']
        subject_email = data_email['assunto']
        body_email = data_email['corpo']

        print(f"Processando e-mail para: {user_email}, Assunto: {subject_email}, Corpo: {body_email}\n\n")


connect_ActiveMQ = stomp.Connection([('localhost', 61613)])  
connect_ActiveMQ.set_listener('', Email_Consumer())
connect_ActiveMQ.connect(wait=True)
connect_ActiveMQ.subscribe(destination='/queue/emails', id=1, ack='auto')

while True:
    pass


    