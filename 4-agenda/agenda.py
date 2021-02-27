#4. Usar POO para criar uma agenda

from agenda_class import agenda_class

#executa as instruções da agenda
lista_agenda = []
instrucao = 0
while instrucao != 4:
        
    instrucao = int(input("Digite o número da opção: 1 - adicionar, 2 - excluir, 3 - imprimir ou 4 - sair: \n"))
    
    #adiciona contatos sem espaços desnecessários
    if instrucao == 1: 
        nome = input("Nome: \n").strip()
        telefone = input("Telefone: \n").strip()
        endereco = input("Endereço: \n").strip()
        ag = agenda_class(nome,telefone,endereco)
        lista_agenda.append(ag)
        print("\nSeu contato foi inserido \n")

    #exclui dados da agenda, mas mantém agenda
    elif instrucao == 2:
        while True:
            contador = 0
            for contato in lista_agenda:
                print(f"{contato.nome, contato.telefone, contato.endereco} - {contador}")
                contador += 1
            print(f"\nSe desistiu, digite {contador} para sair!\n")
            contador_selecionado = input("\n Qual o número da informação deseja excluir?\n")
            if contador_selecionado.isnumeric():
                contador_novo = int(contador_selecionado)
                if contador_novo in range(0, contador):
                    print("\nEstamos excluindo... quase lá...\n")
                    lista_selecionada = lista_agenda.pop(contador_novo) #Apaga o item
                    print(f"\nO dado da agenda {lista_selecionada.nome, lista_selecionada.telefone, lista_selecionada.endereco} foi excluído!\n") #Item foi excluído
                    break #Sai do loop
                elif contador_novo == contador:
                    break   #Sai do loop
                else:
                    print("Informação não existe.")
            else:
                print("Informação incorreta.")
    
    #imprime a agenda
    elif instrucao == 3:
        for contato in lista_agenda:
            print(f"\nContatos da agenda: {contato.nome, contato.telefone, contato.endereco}\n")

    #sai da agenda
    elif instrucao == 4:
        print(f'\n<< Fechamos sua agenda! >>')
        break
    #caso usuário digite opção inexistente
    elif instrucao >=5: 
        print("Essa opção não existe!")
