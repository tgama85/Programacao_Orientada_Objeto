#5. Montar um sistema de cadastro de alunos, 
# professores e cursos usando conjuntos e orientação à objetos

#imports das classes de negócio
from Curso import Curso
from Aluno import Aluno
from Professor import Professor
import sys

#inicialização de variáveis e objetos
lista_opcoes = [   "0-) Sair \n"
                  ,"1-) Ver lista de alunos"
                  ,"2-) Incluir um novo aluno"
                  ,"3-) Excluir um aluno existente"
                  ,"4-) Ver um aluno"
                  ,"5-) Ver lista de professor"
                  ,"6-) Incluir um novo professor"
                  ,"7-) Excluir um professor existente"
                  ,"8-) Ver um professor"
                  ,"9-) Ver lista de cursos"
                  ,"10-) Incluir um novo curso"
                  ,"11-) Excluir um curso existente"
                  ,"12-) Ver um curso"]

lista_professores = []
lista_alunos = []
lista_cursos = []

#Iteração com o usuário e dar as boas vindas
nome_login = input("Olá! Por favor entre com o nome de usuário...\n")

#Loop para manter na memória
while True:
    #Mostrar as boas vindas e as opções
    print(f"Olá! Seja bem-vinde {nome_login}! Escolha uma opção:")
    for opcao in lista_opcoes:
        print(opcao)
    opcao_selecionada = int(input("Escolha uma opção \n"))
    #condicionais para controlar a navegação do programa
    if opcao_selecionada == 0: #Sai do programa
        print("Você saiu do sistema.")
        sys.exit()
    elif opcao_selecionada == 1: #Ver lista de alunos
        for aluno in lista_alunos:
            print(f"Aluno(a): {aluno.nome} - matrícula: {aluno.matricula}")
    elif opcao_selecionada == 2: #Incluir um novo aluno
        
        while True:
            nome_aluno = input("Digite o nome do(a) Aluno(a)\n")
            matricula_aluno = input("Digite a matrícula do(a) Aluno(a)\n")
            documento_aluno = input("Digite o número do documento\n")
            aluno = Aluno(nome=nome_aluno,documento=documento_aluno,matricula=matricula_aluno) #Incluindo o documento no momento do construtor
            lista_alunos.append(aluno) #Insere um aluno na lista
            print(f"O(A) aluno(a) {aluno.nome} foi inserido(a)!")  #Mostra para o usuário que o append foi feito      
            
            #Solicitando a saída para o usuário    
            controle_insert = input("Deseja incluir mais um(a) aluno(a)? (Digite 'n' ou 'N' para sair) \n")
            if len(controle_insert) == 1:
                if controle_insert == "n" or controle_insert == "N" or controle_insert == "S" or controle_insert == "s":
                    if controle_insert.upper() == "N":
                        print("Saindo da inclusão de alunos(as)...")
                        break
        
    elif opcao_selecionada == 3: #Excluir um aluno existente
        
        while True:
            iterador_alunos = 0 
            max_alunos = len(lista_alunos)
            while iterador_alunos < max_alunos: #Outra forma de fazer loop em lista
                print(f"Índice - {iterador_alunos} - aluno(a){lista_alunos[iterador_alunos].nome}")
                iterador_alunos += 1
            input_do_usuario = input("Digite um valor para a exclusão do(a) aluno(a) \n")
            
            if input_do_usuario.isnumeric():
                aluno_selecionado = int(input_do_usuario) #Solicite para o usuário o índice
                if aluno_selecionado in range(0, max_alunos):
                    aluno_excluido = lista_alunos.pop(aluno_selecionado) #pop para excluir o aluno e retornar o objeto excluído
                    print(f"O aluno {aluno_excluido.nome} foi excluído") #mostra para o usuário
                    #Solicitando a saída para o usuário    
                    controle_exclusao = input("Deseja sair da exclusão? (Digite 's' ou 'S' para sair) \n")
                    if len(controle_exclusao) == 1:
                        if controle_exclusao == "n" or controle_exclusao == "N" or controle_exclusao == "S" or controle_exclusao == "s":
                            if controle_exclusao.upper() == "S":
                                print("Saindo da exclusão de alunos(as)...")
                                break
                else:
                    print("Esse valor não existe")
            else:
                print("Esse valor deve ser um número")
                    
    elif opcao_selecionada == 4: #Ver um aluno
        while True:
            nome_aluno_pesquisado = input("Digite o nome do(a) aluno(as) a ser pesquisado \n")
            controle_iteracao = 0
            for aluno in lista_alunos:
                if nome_aluno_pesquisado.upper() in aluno.nome.upper():
                    print(f"O(A) aluno(a) {aluno.nome} com a {aluno.matricula} e o documento {aluno.documento} consta na lista.")
                    controle_iteracao += 1
            if controle_iteracao == 0:
                print("O(A) aluno(a) não foi encontrado(a)")

            #Solicitando a saída para o usuário    
            controle_pesquisa = input("Deseja sair da pesquisa? (Digite 's' ou 'S' para sair) \n")
            if len(controle_pesquisa) == 1:
                if controle_pesquisa == "n" or controle_pesquisa == "N" or controle_pesquisa == "S" or controle_pesquisa == "s":
                    if controle_pesquisa.upper() == "S":
                        print("Saindo da pesquisa de alunos(as)...")
                        break
            
    elif opcao_selecionada == 5: #Ver lista de professor
        for professor in lista_professores:
            print(f"Professor(a): {professor.nome} - disciplina: {professor.disciplina} - matrícula: {professor.matricula}")

    elif opcao_selecionada == 6:    #Incluir um novo professor
        
        while True:
            nome_professor = input("Digite o nome do(a) Professor(a)\n")
            disciplina_professor = input("Digite a disciplina do(a) Professor(a)\n")
            matricula_professor = input("Digite a matrícula do(a) Professor(a)\n")
            professor = Professor(nome=nome_professor,disciplina=disciplina_professor,matricula=matricula_professor) #Incluindo o documento no momento do construtor
            lista_professores.append(professor) #Insere um professor na lista
            print(f"O(A) professor(a) {professor.nome} foi inserido(a)!")  #Mostra para o usuário que o append foi feito      
            
            #Solicitando a saída para o usuário    
            controle_insert_prof = input("Deseja incluir mais um(a) professor(a)? (Digite 'n' ou 'N' para sair) \n")
            if len(controle_insert_prof) == 1:
                if controle_insert_prof == "n" or controle_insert_prof == "N" or controle_insert_prof == "S" or controle_insert_prof == "s":
                    if controle_insert_prof.upper() == "N":
                        print("Saindo da inclusão de professores...")
                        break

    elif opcao_selecionada == 7: #Excluir um professor existente
         
        while True:
            iterador_professores = 0 
            max_professores = len(lista_professores)
            while iterador_professores < max_professores: #Outra forma de fazer loop em lista
                print(f"Índice - {iterador_professores} - professor(a): {lista_professores[iterador_professores].nome}")
                iterador_professores += 1
            input_do_usuario = input("Digite um valor para a exclusão do(a) professor(a) \n")
            
            if input_do_usuario.isnumeric():
                professor_selecionado = int(input_do_usuario) #Solicite para o usuário o índice
                if professor_selecionado in range(0, max_professores):
                    professor_excluido = lista_professores.pop(professor_selecionado) #pop para excluir o professor e retornar o objeto excluído
                    print(f"O(A) professor(a) {professor_excluido.nome} foi excluído(a)") #mostra para o usuário
                    #Solicitando a saída para o usuário    
                    controle_exclusao_prof = input("Deseja sair da exclusão? (Digite 's' ou 'S' para sair) \n")
                    if len(controle_exclusao_prof) == 1:
                        if controle_exclusao_prof == "n" or controle_exclusao_prof == "N" or controle_exclusao_prof == "S" or controle_exclusao_prof == "s":
                            if controle_exclusao_prof.upper() == "S":
                                print("Saindo da exclusão de professores...")
                                break
                else:
                    print("Esse valor não existe")
            else:
                print("Esse valor deve ser um número")

    elif opcao_selecionada == 8: #Ver um professor
        while True:
            nome_professor_pesquisado = input("Digite o nome do(a) professor(a) a ser pesquisado \n")
            controle_iteracao_prof = 0
            for professor in lista_professores:
                if nome_professor_pesquisado.upper() in professor.nome.upper():
                    print(f"O(A) professor(a) {professor.nome} com a matrícula {professor.matricula} e a discplina {professor.disciplina} consta na lista.")
                    controle_iteracao_prof += 1
            if controle_iteracao_prof == 0:
                print("O(A) professor(a) não foi encontrado(a)")

            #Solicitando a saída para o usuário    
            controle_pesquisa_prof = input("Deseja sair da pesquisa? (Digite 's' ou 'S' para sair) \n")
            if len(controle_pesquisa_prof) == 1:
                if controle_pesquisa_prof == "n" or controle_pesquisa_prof == "N" or controle_pesquisa_prof == "S" or controle_pesquisa_prof == "s":
                    if controle_pesquisa_prof.upper() == "S":
                        print("Saindo da pesquisa de professores...")
                        break

    elif opcao_selecionada == 9: #Ver lista de cursos
        for curso in lista_cursos:
            print(f"Curso: {curso.nome} - período: {curso.periodo}")

    elif opcao_selecionada == 10: #Incluir um novo curso
        
        while True:
            nome_curso = input("Digite o nome do Curso\n")
            periodo_curso = input("Digite o período do Curso\n")
            curso = Curso(nome=nome_curso,periodo=periodo_curso) #Incluindo o curso no momento do construtor
            lista_cursos.append(curso) #Insere um curso na lista
            print(f"O curso {curso.nome} foi inserido!")  #Mostra para o usuário que o append foi feito      
            
            #Solicitando a saída para o usuário    
            controle_insert_curso = input("Deseja incluir mais um curso? (Digite 'n' ou 'N' para sair) \n")
            if len(controle_insert_curso) == 1:
                if controle_insert_curso == "n" or controle_insert_curso == "N" or controle_insert_curso == "S" or controle_insert_curso == "s":
                    if controle_insert_curso.upper() == "N":
                        print("Saindo da inclusão de cursos...")
                        break

    elif opcao_selecionada == 11: #Excluir um curso existente
            
        while True:
            iterador_cursos = 0 
            max_cursos = len(lista_cursos)
            while iterador_cursos < max_cursos: #Outra forma de fazer loop em lista
                print(f"Índice - {iterador_cursos} - curso: {lista_cursos[iterador_cursos].nome}")
                iterador_cursos += 1
            input_do_usuario = input("Digite um valor para a exclusão do curso \n")
            
            if input_do_usuario.isnumeric():
                curso_selecionado = int(input_do_usuario) #Solicite para o usuário o índice
                if curso_selecionado in range(0, max_cursos):
                    curso_excluido = lista_cursos.pop(curso_selecionado) #pop para excluir o curso e retornar o objeto excluído
                    print(f"O curso {curso_excluido.nome} foi excluído") #mostra para o usuário
                    #Solicitando a saída para o usuário    
                    controle_exclusao_curso = input("Deseja sair da exclusão? (Digite 's' ou 'S' para sair) \n")
                    if len(controle_exclusao_curso) == 1:
                        if controle_exclusao_curso == "n" or controle_exclusao_curso == "N" or controle_exclusao_curso == "S" or controle_exclusao_curso == "s":
                            if controle_exclusao_curso.upper() == "S":
                                print("Saindo da exclusão de cursos...")
                                break
                else:
                    print("Esse valor não existe")
            else:
                print("Esse valor deve ser um número")

    elif opcao_selecionada == 12: #Ver um curso
        while True:
            nome_curso_pesquisado = input("Digite o nome do curso a ser pesquisado \n")
            controle_iteracao_curso = 0
            for curso in lista_cursos:
                if nome_curso_pesquisado.upper() in curso.nome.upper():
                    print(f"O curso {curso.nome} com o período {curso.periodo} consta na lista.")
                    controle_iteracao_curso += 1
            if controle_iteracao_curso == 0:
                print("O curso não foi encontrado")

            #Solicitando a saída para o usuário    
            controle_pesquisa_curso = input("Deseja sair da pesquisa? (Digite 's' ou 'S' para sair) \n")
            if len(controle_pesquisa_curso) == 1:
                if controle_pesquisa_curso == "n" or controle_pesquisa_curso == "N" or controle_pesquisa_curso == "S" or controle_pesquisa_curso == "s":
                    if controle_pesquisa_curso.upper() == "S":
                        print("Saindo da pesquisa de cursos...")
                        break