#privado é dois __
#protegido é um _
class Empresa:
    def __init__(self, nome, telefone="", email="", quantidade_funcionario=0):
        self._nome = nome
        self.__telefone = telefone
        self._email = email
        self._quantidade_funcionario = quantidade_funcionario


    def get_nome(self):
        return self._nome

    def get_quantidade_funcionario(self):
        return self._quantidade_funcionario

    def set_quantidade_funcionario(self, quantidade_funcionario):
        if quantidade_funcionario < 0:
            print("Quantidade de funcionários inválida!")

        else:
            self._quantidade_funcionario = quantidade_funcionario

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self._email

    def apresentar(self):
        print(f'A empresa se chama {self._nome}', f'e para entrar em contato digite:{self.__telefone}',
              f'ou mande um email para: {self._email}.',
              f'A empresa tem {self._quantidade_funcionario} funcionários.')

empresa_1 = Empresa('Pandora', '18996062236', 'pandora@gmail.com', 100)
empresa_2 = Empresa('Sephora', '18996062656', 'sephora@gmail.com', 125)


#Get- receber informação
#Set- envia informação
#Is- verificação
class Setor(Empresa):
    def __init__(self, nome, area):
        super().__init__(nome)
        self.area = area
        self._ativo = True


    def apresentar(self):
        print(f'O setor é {self._nome}', f' e é da área {self.area}.')

    #Está recebendo informação
    def get_ativo(self):
        return self._ativo

    #Está enviando informação
    def set_ativar(self, status):
        #(se o setor está ativo e se eu quero ativar)
        if self._ativo and status:
            print('O setor já está ativo!')

        elif not self._ativo and status:
            self._ativo = status
            print("O setor se tornou ativo!")

        elif self._ativo and not status:
            self._ativo = status
            print("O setor foi desativado!")

        else:
            print('O setor já está desativo!')

setor_1 = Setor('Financeiro', 'finanças')
setor_2 = Setor('Gestão pública', 'pessoas')
