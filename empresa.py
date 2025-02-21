class Empresa:
    def __init__(self, nome, telefone, email, quantidade_funcionario):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.quantidade_funcionario = quantidade_funcionario

    def apresentar(self):
        print(f'A empresa se chama {self.nome}', f'e para entrar em contato digite:{self.telefone}',
              f'ou mande um email para: {self.email}.',
              f'A empresa tem {self.quantidade_funcionario} funcionários.')

empresa_1 = Empresa('Pandora', '18996062236', 'pandora@gmail.com', 100)
empresa_2 = Empresa('Sephora', '18996062656', 'sephora@gmail.com', 125)

class Setor(Empresa):
    def __init__(self, nome, area):
        super().__init__(nome, email=False, quantidade_funcionario=False, telefone=False)
        self.area = area
        self.ativo = True


    def apresentar(self):
        print(f'O setor é {self.nome}', f' e é da área {self.area}.')

        if self.ativo:
            print('O setor está ativo!')

        else:
            print('O setor não está ativo!')

    def ativar(self):
        if self.ativo:
            print('O setor já está ativo!')

        else:
            print('O setor está desativo!')

setor_1 = Setor('Financeiro', 'finanças')
setor_2 = Setor('Gestão pública', 'pessoas')
