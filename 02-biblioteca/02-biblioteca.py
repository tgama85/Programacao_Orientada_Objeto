#2. Fazer um sistema de biblioteca (Deve imprimir 
# uma lista com 10 livros, pedir o nome do solicitante 
# do empréstimo, pedir para selecionar um livro e 
# imprimir o livro selecionado)-Criar usando classes

from biblioteca_class import biblioteca_class

livro_0 = biblioteca_class("O universo numa casca de noz")
livro_1 = biblioteca_class("Uma breve história do tempo")
livro_2 = biblioteca_class("O grande projeto")
livro_3 = biblioteca_class("A teoria de tudo")
livro_4 = biblioteca_class("Buracos Negros: Palestra da BBC Reith Lectures")
livro_5 = biblioteca_class("Uma nova história do tempo")
livro_6 = biblioteca_class("Breves respostas para grandes questões")
livro_7 = biblioteca_class("Infinito em todas as direções")
livro_8 = biblioteca_class("O livro que ninguém leu")
livro_9 = biblioteca_class("Mundos em Guerra: a luta de mais 2.500 anos entre o Oriente e o Ocidente")

print("Bem-vinde a Biblioteca Gama! Os livros para empréstimo são:"
'''
        [0] O universo numa casca de noz',
        [1] Uma breve história do tempo',
        [2] O grande projeto',
        [3] A teoria de tudo',
        [4] Buracos Negros: Palestra da BBC Reith Lectures',
        [5] Uma nova história do tempo',
        [6] Breves respostas para grandes questões',
        [7] Infinito em todas as direções',
        [8] O livro que ninguém leu',
        [9] Mundos em Guerra: a luta de mais 2.500 anos entre o Oriente e o Ocidente.''')

usuario = input("Por favor digite seu nome para realizarmos o empréstimo: ") #nome do usuario
emprestimo = int(input("Digite o número do livro desejado: ")) #solicitações do usuário (seleção)

   #lista para seleção
lista_livros = [livro_0,
        livro_1,
        livro_2,
        livro_3,
        livro_4,
        livro_5,
        livro_6,
        livro_7,
        livro_8,
        livro_9]    #lista para escolha
opcao_selecionada = int(emprestimo)
for opcao in lista_livros:    
        if opcao_selecionada >= 10:    #caso usuário não digite a opção correta
                print("Não temos esta opção em nosso acervo.")
                break
        if opcao_selecionada <= 9:     #verifica a seleção
                print(f"{usuario} o empréstimo do livro {lista_livros[opcao_selecionada].emprestimo} foi realizado.") #resultado
                print("Volte sempre!")
                break