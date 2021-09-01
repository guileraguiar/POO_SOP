'''


EM DESENVOLVIMENTO


Alunos: Davi Rafael Longhi, Filipe José Junks e Guilherme de Aguiar
Curso: Sistemas de Informação
Turma: 2021/01
Sistema Operacional
Linguagem: Python
Desenvolva os algoritmos de alocação de particação Best-Fit, Worst-Fit e First-Fit.

Considere que seu algoritmo receba por parâmetro a configuração da memória, onde neste exemplo o X representa um local alocado e 0 um local livre.

[ X, 0, 0, 0, 0, 0, X, 0, 0, X, X, X, 0, 0, X]

O seu algoritmo irá receber também a coleção de processos a ser alocado na memória. Por exemplo:

[ 2 , 4, 1, 2]

Onde os números representam o tamanho de cada processo.

O seu algoritmo deverá alocar todos os processos na memórias de acordo com a estratégia escolhida.

O seu programa deverá imprimir a configuração da memória a cada alocação.

Caso não seja possível alocar o processo, o programa deverá informar.

O programa poderá ser desenvolvido com qualquer linguagem de programação.

'''

import random

print("==============================")
print("   Configuração de Memória")
print("==============================\n")

print("Digite o tamanho da coleção.")
tamanhocolecao = int(input())

colecao = [' '] * tamanhocolecao

for i in range(0, tamanhocolecao):
    print("\nDigite o tamanho do processo", i + 1)
    colecao[i] = int(input())

print("\nAgora, digite o tamanho da memória.")
tamanhomemoria = int(input())

memoria = [' '] * tamanhomemoria
opcao = 0
tamanho = 0
letra = ''
for i in range(0,tamanhomemoria):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'X'
    else:
        memoria[i] = ' '

#Aqui você deve imprimir todo o conteúdo da variável memória
print("========================")
print("        Memória         ")
print("========================")
for i in range(0,tamanhomemoria):
    print(memoria[i], end="|")

while(opcao != 4):
    #Menu do programa
    print("\n1 - First-Fit")
    print("2 - Best-Fit")
    print("3 - Worst-Fit")
    print("4 - Sair")
    print()
    print("Escolha o algoritmo pelo número.")
    opcao = int(input())
    print()
    if opcao == 4:
        print("O programa foi finalizado com sucesso!")
        break
    print("Digite a letra a ser utilizada.")
    letra = input()
    print()

    contador1 = 0
    if(opcao == 1):
      for i in range(0, tamanhocolecao):
        contador1 += 1
        #Implemente aqui a lógica do FIRST FIT
        #Para fazermos a lógica da primeira escolha, é necessário criarmos variáveis de posições e nisso fazer o inicio e fim para calcular o tamanho do buraco, e tentar através do algoritmo, achar no meio sortido o primeiro espaço sufiente para suportar o tamanho da informação que será alocada na memória
        posicao1 = 0
        posicao2 = 0
        tamanhoburaco = 0
        inicio = 0
        fim = 0
        fiminf = 0
        #como são 100 posições na memória temos que contar a posição até 99, ou seja, menor que 100, pois o algoritmo conta o número 0 como a primeira posição. 
        #Aqui nesse primeiro while acharemos o inicio do buraco.
        while (posicao1 < tamanhomemoria):
            achou1 = False
            if memoria[posicao1] == ' ':
                inicio = posicao1
                posicao2 = inicio + 1
                #usaremos um outro while para encontrar o final do buraco, subtraindo o fim do inicio para encontrar o tamanho total.
                while(posicao2 < tamanhomemoria):
                    if memoria[posicao2] != ' ':
                        fim = posicao2
                        tamanhoburaco = fim - inicio
                        #Quando encontrar o primeiro buraco que caiba a informação, preencherá todo com o for.
                        if tamanhoburaco >= colecao[i]:
                            fiminf = inicio + tamanho
                            for i in range(inicio,fim): 
                                memoria[i] = letra
                                achou1 = True
                        break
                    posicao2 += 1
            posicao1 += 1
            #quando achar o buraco e salvar a informação nele, mostrará novamente a memória, porém atualizada, quebrando para o usuário fazer novos preenchimentos enquanto nao digitar o número correto para finalizar o programa.
            if achou1 == True:
                break
            #Caso a informação seja insuficiente para caber em algum buraco do algoritmo, o programa mostrará uma mensagem de erro para o usuário tentar novamente, também quebrará para que seja possível fazer novas tentativas.
            if posicao2 == tamanhomemoria and achou1 == False:
                print("Erro! Não há espaço suficiente na memória para suportar o tamanho da sua informação, por favor, tente novamente!")
                print()
                break
    else:
        if (opcao == 2):
          for i in range (0, tamanhocolecao):
            #Implemente aqui a lógica da melhor escolha
            #Para fazermos a lógica da melhor escolha, é necessário criarmos variáveis de posições e nisso fazer o inicio e fim para calcular o tamanho do buraco, e tentar através do algoritmo, achar no meio sortido o menor espaço sufiente para suportar o tamanho da informação que será alocada na memória
            posicao1 = 0
            posicao2 = 0
            tamanhoburaco = 0
            inicio = 0
            fim = 0
            omenorburaco = 0
            iniciomenor = 0
            fimmenor = 0
            contburaco = 0
            fimtamanho = 0
            #como são 100 posições na memória temos que contar a posição até 99, ou seja, menor que 100, pois o algoritmo conta o número 0 como a primeira posição. 
            #Aqui nesse primeiro while acharemos o inicio do buraco.
            while(posicao1 < tamanhomemoria):
                achou2 = False
                if memoria[posicao1] == ' ':
                    inicio = posicao1
                    posicao2 = inicio + 1
                    #usaremos um outro while como posição para encontrar o final do buraco, subtraindo o fim do inicio para encontrar o tamanho total. Contaremos o primeiro buraco também para podermos fazer a lógica do menor buraco suficiente.
                    while(posicao2 < tamanhomemoria):
                        if memoria[posicao2] != ' ':
                            fim = posicao2
                            tamanhoburaco = fim - inicio
                            if tamanhoburaco >= colecao[i]:
                                contburaco += 1
                                if contburaco == 1:
                                    omenorburaco = tamanhoburaco
                                    achou2 = True
                                    iniciomenor = posicao1
                                    fimmenor = posicao2
                                    fimtamanho = iniciomenor + tamanho
                                else:
                                    if tamanhoburaco < omenorburaco:
                                        omenorburaco = tamanhoburaco
                                        achou2 = True
                                        iniciomenor = posicao1
                                        fimmenor = posicao2
                                        fimtamanho = iniciomenor + tamanho
                            break
                        posicao2 += 1
                posicao1 += 1
                #Caso percorra todo o código e ache o menor buraco que caiba a inmformação, ele imprime na tela.
                if posicao2 == tamanhomemoria and achou2 == True:
                    for i in range(iniciomenor,fimmenor):
                        memoria[i] = letra
                        achou2 = True
                        break
                #Caso não, mostra a mensagem de erro ao usuário retornando ao início para tentar novamente caso queira.
                else:
                    print("Error! Não há espaço suficiente na memória para suportar o tamanho da sua informação, por favor, tente novamente!")
                    print()
                    break
        else:
            if(opcao == 3):
                #Implemente aqui a lógica da pior escolha
                #Para fazermos a lógica da pior escolha, é necessário criarmos variáveis de posições e nisso fazer o inicio e fim para calcular o tamanho de cada buraco, e tentar através do algoritmo, achar no meio sortido o maior espaço sufiente para suportar o tamanho da informação que será alocada na memória
                posicao1 = 0
                posicao2 = 0
                tamanhoburaco = 0
                inicio = 0
                fim = 0
                omaiorburaco = 0
                fimmaior = 0
                iniciomaior = 0
                #como são 100 posições na memória temos que contar a posição até 99, ou seja, menor que 100, pois o algoritmo conta o número 0 como a primeira posição. 
                #Aqui nesse primeiro while acharemos o inicio do buraco.
                while(posicao1 < tamanhomemoria):
                    achou3 = False
                    if memoria[posicao1] == ' ':
                        inicio = posicao1
                        posicao2 = inicio + 1
                        #usaremos um outro while para encontrar o final do buraco, subtraindo o fim do inicio para encontrar o tamanho total.
                        while(posicao2 < 100):
                            #Quando a memória for diferente de "vazio", o programa entende que é o fim do buraco, fazendo o calculo par asaber o tamanho.
                            if memoria[posicao2] != ' ':
                                fim = posicao2
                                tamanhoburaco = fim - inicio
                                #Aqui foi feito a lógica do maior para sempre gravar na variável "omaiorburaco" quando o tamanho do buraco for maior e ai vai quebrar para testar se possui algum outro lugar com tamanho maior. 
                                if tamanhoburaco > \
                                omaiorburaco:
                                    iniciomaior = posicao1
                                    fimmaior = iniciomaior + tamanho
                                    omaiorburaco = tamanhoburaco
                                break
                            posicao2 += 1
                    posicao1 += 1
                    #Quando chegar no final do programa testando, e omaiorburaco for maior ou igual ao tamanho da informação, será gravada a letra na memória e então quebrará para o usuário dar continuidade.
                    if posicao2 == tamanhomemoria and omaiorburaco >= tamanho:
                        for i in range(iniciomaior,fimmaior):
                            memoria[i] = letra
                            achou3 = True
                        break
                    #Caso chegue no final e o algoritmo não tenha encontrado nenhum lugar suficiente para suportar a memória, o programa apresentará uma mensagem de erro e retornará ao usuário para tentar novamente.
                    if posicao2 == tamanhomemoria and achou3 == False:
                        print("Error! Não há espaço suficiente na memória para suportar o tamanho da sua informação, por favor, tente novamente!")
                        print()
                        break


    # Aqui você deve imprimir todo o conteúdo da variável memória
    for i in range(0,tamanhomemoria):
        print(memoria[i], end="|")
