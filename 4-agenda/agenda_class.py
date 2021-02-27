class agenda_class:
    instrucao = 0
    def __init__(self,nome,telefone,endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        agenda_class.instrucao += 1