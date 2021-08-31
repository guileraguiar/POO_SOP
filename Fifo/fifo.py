# Universidade da Região de Joinville - UNIVILLE

# Alunos: Davi Rafael Longhi, Filipe José Junks e Guilherme de Aguiar Correa
# Professor: Leanderson André
# Curso: Sistemas Operacionais
# Tema: Simulador de Escalonador FIFO
# Criar um simulador de escalonamento estilo FIFO, que simule por prioridades.

conttempocorrente = 0
tempocorrente = 0
contprocesso = 0
contprocesso2 = 0
qtdeprocesso = 3
tempoexecucao = [3,5,1]
tempoprocesso = 0
tempototal = 9
processo = ["A", "B", "C"]
prioridade = [2,5,3]
listadefinalizados = [0] * qtdeprocesso

prioridade.sort(reverse = True)

# O QUE FALTA FAZER ??
# Criar uma forma de colocar o nome do processo no código para mostrar qual processo ta sendo escalonado
# Criar uma forma de colocar o processo que ja foi finalizado na lista de processos finalizados

# Para isso precisamos criar lógicas, tentar criar funções talvez

print("-------------------------------")
print("SIMULADOR DE ESCALONAMENTO FIFO")
print("-------------------------------")

def finalizados():
  global tempoprocesso
  for i in range(0,3):
    # aqui é uma forma de acessar cada prioridade pelo range
    # o tempoprocesso vai servir como contador para saber se atingiu o tempo deexecuçãodo procesos que foi escalonado, enquanto o tempoprocesso que seria umcontador formaior que o tempoexecucao[i] quer dizer que ele já completou tudo efoi finalizadoe ai mostraria na lista de processos finalizados
    # é uma ideia que precisa ser melhorada e finalizada
    if prioridade[i] < tempototal:
        tempoprocesso += 1
        if tempoprocesso > tempoexecucao[i]:
            print(processo[i])
            tempoprocesso = 0
  return # colocar algo pra retornar

def escalonado():
  global tempoprocesso
  for i in range(0,3):
    # aqui é uma forma de acessar cada prioridade pelo range
    # o tempoprocesso vai servir como contador para saber se atingiu o tempo de execução dos processos que foi escalonado, enquanto o tempoprocesso que seria um contador for menor ou igual que o tempoexecucao[i] ele continua printando que o processo[i] está escalonado, mas quando o tempoprocesso for igual aotempoexecução, ele zera o contador tempoprocesso, para que possa pular para o proximo processo a ser escalonado,onde vai printar o proximo processo em tela,e quando o contador atingir o tempo de execução, ele zera novamente e assim sucessivamente.
    # é uma ideia que precisa ser melhorada e finalizada
    if prioridade[i] < tempototal:
        tempoprocesso += 1
        if tempoprocesso <= tempoexecucao[i]:
            print(processo[i])
            # tem que fazer uma forma da lista do processo ficar na mesma ordem que alista de prioridade, onde prioridade [5,3,2] e processo [B,C,A]
            if tempoprocesso == tempoexecucao[i]:
                tempoprocesso = 0
  return # colocar algo pra retornar

while conttempocorrente < tempototal:
  contprocesso += 1
  contprocesso2 += 1
  

  print("Tempo Corrente: ", conttempocorrente)
  conttempocorrente += 1
  print("Lista de Execução por Prioridade: ", prioridade)
  print("Lista de Finalizados: ", finalizados() )
  print("-----------------------------------------")
  
  print("O processo # ", escalonado(), " foi escalonado \n") 

print("O Simulador terminou toda sua execução!")