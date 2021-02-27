from Pessoa import Pessoa
class Professor(Pessoa):

    def __init__(self,nome,disciplina,matricula):
        self.nome = nome
        self.disciplina = disciplina
        self.matricula = matricula