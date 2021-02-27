from Pessoa import Pessoa
class Aluno(Pessoa):

    def __init__(self, documento, nome, matricula):
        self.documento = documento
        self.nome = nome #Atributos da classe pai
        self.matricula = matricula #Atributos da classe pai