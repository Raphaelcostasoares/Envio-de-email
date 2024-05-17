import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#Código para envio de email em massa

clients = pd.read_excel('./clientes.xlsx')

for index, client in clients.iterrows():
    msg = MIMEMultipart()
    #INFORME O ASSUNTO DO EMAIL
    msg['Subject'] = 'EMAIL SUBJECT :'
    #INFORME O EMAIL REMETENTE
    msg['From'] = 'EMAIL FROM'
    msg['To'] = client['email']
    message = f'Olá {client['nome']}, WRITE MESSAGE  '#ESCREVA A MENSAGEM
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls()
    #Coloque a senha do seu email, caso dê erro crie uma senha de aplicativo no google.
    server.login('YOUR EMAIL', 'YOU PASSWORD')#INFORME EMAIL E SENHA
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()