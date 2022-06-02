from datetime import datetime

print('\n#####################################################')
# exemplo de classe


class Pessoa:
    def __init__(self, nome, ano_nasc, peso, altura):
        self.nome = nome
        self.ano_nasc = ano_nasc
        self.peso = peso
        self.altura = altura

        # self.ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
        # ou
        self.ano_atual = int('{:%Y}'.format(datetime.now()))
        self.idade = self.ano_atual - self.ano_nasc

    def imc(self) -> float:
        return self.peso / (self.altura ** 2)


p = Pessoa("Eduard", 1983, 77, 1.83)
print(f'{p.nome} possui IMC de {p.imc():.2f}')
print(f'{p.nome} tem {p.idade} anos.')

print('\n#####################################################')
# exemplo de Herança


class Programmer(Pessoa):
    def __init__(self, nome, ano_nasc, peso, altura, language, wpm, experience):
        super().__init__(nome, ano_nasc, peso, altura)
        self.language = language
        self.wpm = wpm
        self.experience = experience

    def getCurriculumStr(self):
        return f'Prog. {self.nome} programs in {self.language} and has {self.experience} years of exp.'


prog = Programmer("Luke", 1866, 105, 2.15, "Node.js", 585, 55)
print("Calling Class function: ", prog.getCurriculumStr())
print("Calling parent Class func.: {:.3f}".format(prog.imc()))
