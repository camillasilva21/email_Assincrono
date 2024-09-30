import stomp
import json

class Email_Producer:
    def __init__(self, host, port):
        self.connect_ActiveMQ = stomp.Connection([(host, port)])
        self.connect_ActiveMQ.connect(wait=True)

    def send_email(self, destinatario, assunto, corpo):
        mensagem = {
            "destinatario": destinatario,
            "assunto": assunto,
            "corpo": corpo
        }

        self.connect_ActiveMQ.send(body=json.dumps(mensagem), destination='/queue/emails')
        print("E-mail enviado com sucesso!")

    def close_connection(self):
        self.connect_ActiveMQ.disconnect()


def main(): 
    print("Sistema de envio de e-mails\n\n")
    email = input("Digite e-mail do destinatario\n\n")
    assunto = input("Digite o assunto do e-mail\n\n")
    corpo = input("Digite o corpo do e-mail\n\n")


    email_producer = Email_Producer('localhost', 61613)  
    email_producer.send_email(email, assunto, corpo)
    email_producer.close_connection()

main()