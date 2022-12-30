import smtplib
import email.message

def gen_message():
    ""

def enviar_email():
    corpo_email = open(fr'utils\mail.html').read().format() #variaveis dentro do format

    msg = email.message.Message()
    msg['Subject'] = "Teste de Alerta"
    msg['From'] = 'ictlatam.sencinet@gmail.com'
    msg['To'] = 'renato.almeida@sencinet.com'
    password = 'iejameeocrynccvi'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()