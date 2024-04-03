class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome}!")

    def aniversario(self):
        self.idade += 1


class Funcionario(Pessoa):
    def __init__(self, nome, idade, profissao, salario, departamento):
        super().__init__(nome, idade, profissao)
        self.salario = salario
        self.departamento = departamento

    def promover(self, novo_salario):
        self.salario = novo_salario
        print(f"{self.nome} foi promovido! Novo salário: R${self.salario:.2f}")

    def transferir(self, novo_departamento):
        self.departamento = novo_departamento
        print(f"{self.nome} foi transferido para o departamento de {self.departamento}.")


# Exemplo de uso:
funcionario1 = Funcionario("João", 25, "Desenvolvedor", 5000.00, "TI")
funcionario2 = Funcionario("Maria", 30, "Analista de Negócios", 7000.00, "Comercial")

funcionario1.cumprimentar()
funcionario1.aniversario()
print(f"Idade de {funcionario1.nome}: {funcionario1.idade}")
funcionario1.promover(6000.00)
funcionario1.transferir("Recursos Humanos")


funcionario2.cumprimentar()
funcionario2.aniversario()
print(f"Idade de {funcionario2.nome}: {funcionario2.idade}")
funcionario2.promover(8000.00)
funcionario2.transferir("Marketing")
