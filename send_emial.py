import os 
import smtplib
from email.message import EmailMessage
from account import Account


#configurar e-mail
class Send_Email():
    def send_email(self,):
        self.test = Account().info_Account()
        try:
# Criando o E-mail
            msg = EmailMessage()
            msg['Subject'] = self.test[2]
            msg['From'] = self.test[0]
            msg['To'] = self.test[3]
            msg.set_content(self.test[4])

# Enviar E-mail:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.test[0], self.test[1])
                smtp.send_message(msg)
        except:
            print("ERRO AO ENVIAR E-MAIL")

# test = Send_Email()
# print(test.send_email())