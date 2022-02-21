class Account():

    def info_Account(self, ):
        self.account = ()

        name = str(input("Digite seu e-mail: "))
        password = str(input("Digite sua senha: "))
        subject = str(input("Digite o assunto do e-mail: "))
        destinatario = str(input("Digite o destinatario: "))
        mensagem = str(input("Digite a mensagem: "))

        self.account = name, password, subject, destinatario, mensagem

        return self.account

# test = Account()
# print(test.info_Account())