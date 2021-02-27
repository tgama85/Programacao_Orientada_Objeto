#1. Fazer um cadastro de viagem (Deve pedir o nome do 
# viajante, dar as opções de destino e imprimir a 
# selecionada)-Criar usando classes

from viagem_class import viagem_class

viagem_0 = viagem_class("Flórida")
viagem_1 = viagem_class("Havaí")
viagem_2 = viagem_class("Tóquio")
viagem_3 = viagem_class("Egito")
viagem_4 = viagem_class("Londres")

print("Bem-vinde! Viagens Gama tem algumas ofertas para você!")
viajante = input("Digite seu nome para começarmos: ")
print(f"{viajante} temos 5 destinos que combinam com você:"
'''
[0] Flórida
[1] Havaí
[2] Tóquio
[3] Egito
[4] Londres''')

selecao = int(input("Selecione o número da viagem desejada: "))   #solicitação ao usuário
lista_viagem = [viagem_0, viagem_1, viagem_2, viagem_3, viagem_4]     #lista dos índices dos objetos para escolha
opcao_selecionada = int(selecao)
for opcao in lista_viagem:
    if opcao_selecionada >= 5:    #caso usuário não digite a opção correta
        print("Esta opção não está incluída em nossos destinos.")
        break
    if opcao_selecionada <= 4:     #verifica a seleção
        print(f"{viajante} sua viagem para {lista_viagem[opcao_selecionada].destino} está marcada.") #resultado
        print("Volte sempre!")
        break