import java.nio.file.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;
import java.nio.charset.StandardCharsets;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.io.*;

/*
Desenvolva um aplicativo para auxiliar na organização financeira pessoal.
O aplicativo deverá armazenar os valores das despesas e ganhos e calcular o saldo atual. As despesas deverão ser amarzenados em um arquivo chamado despesas.dat. Os ganhos deverão ser salvos em um arquivo chamado ganhos.dat.
O saldo atual corresponderá a soma de todos os ganhos menos as despesas (GANHOS - DESPESAS). O calculo do saldo atual deverá ser realizado em memória e empresado em tela.
Novas entradas de despesas e ganhos podem ser cadastrado pelo usuário. Não se é necessário ter opção de excluir ou atualizar os valores de ganhos e despesas.
Desenvolva o diagrama de classes UML da solução desenvolvida.
Utilize todos os seus conhecimentos em orientação a objetos para desenvolver o aplicativo.
*/

public class Main {

    public static void main(String[] args) {
        int opcao = 0;
        Scanner input = new Scanner(System.in);

        while (opcao != 4){
            System.out.println("\n======================");
            System.out.println("Organização Financeira");
            System.out.println("======================\n");

            System.out.println("Escolha uma opção abaixo");
            System.out.println("========================\n");

            System.out.println("1 - Adicionar ganhos");
            System.out.println("2 - Adicionar despesas");
            System.out.println("3 - Realizar cálculo");
            System.out.println("4 - Sair\n");

            opcao = input.nextInt();

            if (opcao == 1){
                int qtde = 0;
                int cont = 0;
                String receita = " ";               
                System.out.println("\nDigite a quantidade de ganhos que você salvará no arquivo.");
                qtde = input.nextInt();
                input.nextLine();
                while (cont < qtde){
                    cont += 1;                    
                    try{ 
	                    List<String> ganhos = new ArrayList();
                        System.out.println("\nDigite o ganho N°" + cont);
                        receita = input.nextLine();
                        ganhos.add(receita);
	                    Files.write(Paths.get("ganhos.dat"), ganhos, StandardCharsets.UTF_8, StandardOpenOption.APPEND); 
	                }catch(Exception e){ 
	                    e.printStackTrace(); 
	                }
                }  
            }else if (opcao == 2){
                int qtde = 0;
                int cont = 0;
                String custo = "";            
                System.out.println("\nDigite a quantidade de despesas que você salvará no arquivo.");
                qtde = input.nextInt();
                input.nextLine();
                while (cont < qtde){
                    cont = cont + 1;                    
                    try{ 
	                    List<String> despesas = new ArrayList<>();
                        System.out.println("\nDigite a despesa N°" + cont);
                        custo = input.nextLine();
                        despesas.add(custo);
	                    Files.write(Paths.get("despesas.dat"), 
                        despesas, 
                        StandardCharsets.UTF_8, StandardOpenOption.APPEND); 
	                }catch(Exception e){ 
	                    e.printStackTrace(); 
	                }
                }  
            }else if (opcao == 3){
                try{
                    double convert = 0;
                    double totaldespesa = 0; 
                    double saldoatual = 0;
                    List<String> despesas = Files.readAllLines(Paths.get("despesas.dat"));
                    for (String despesa : despesas){
                        //List<Double> despesadouble = new ArrayList<>();
                        convert = Double.parseDouble(despesa);
                        //despesadouble.add(convert);
                        totaldespesa += convert;
                    }
                    System.out.println("\nTotal de despesas: " + totaldespesa);

                    double convertganho = 0;
                    double totalganho = 0; 
                    List<String> ganhos = Files.readAllLines(Paths.get("ganhos.dat"));
                    for (String ganho : ganhos){
                        //List<Double> ganhodouble = new ArrayList<>();
                        convertganho = Double.parseDouble(ganho);
                        //ganhodouble.add(convertganho);
                        totalganho += convertganho;
                    }
                    System.out.println("Total de ganhos: " + totalganho);

                    saldoatual = totalganho - totaldespesa;

                    System.out.println("O saldo atual é: " + saldoatual);

                }catch(Exception e){ 
                    e.printStackTrace(); 
                }
            }else if(opcao == 4){
                System.out.println("\nO programa foi finalizado com sucesso!");
                break;
            }else {
                System.out.println("\nVocê digitou um número inválido!\n");
            }
        }
    }
}
