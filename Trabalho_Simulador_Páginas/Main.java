import java.util.Scanner;

/*Desenvolva o algoritmo de política de substituição de páginas NRU (Not-Recently-Used).
O seu programa deverá simular a carga e a substituição de páginas.
Considere um sistema que tenha 5 páginas.
O programa poderá ser desenvolvido com qualquer linguagem de programação.*/

class Main {
  public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
    
        int memoria[] = new int[5];
        int qtdepagina = 0;
        int pagefault = 0;

        System.out.println("==========================");
        System.out.println("== Simulador de Páginas ==");
        System.out.println("==========================");

        System.out.println("Digite a quatidade de páginas que terá o sistema.");
        qtdepagina = input.nextInt();
        int paginas[] = new int[qtdepagina];

        for (int i = 0; i < qtdepagina; ++i){
            System.out.println("\nDigite o número da página " + (i+1));
            paginas[i] = input.nextInt();
            if (i < 5){
                memoria[i] = paginas[i];
            }
        }


        for (int i = 0; i < qtdepagina; ++i){
            System.out.println("\nPagina Carregada: " + memoria[i]);
            if (i <= 5) {
                System.out.println("Page Faults: " + 0);
            }else{
                if (memoria[i] == paginas[i]){
                    System.out.println("Page Faults: " + pagefault);
                }else{
                    memoria[i] = paginas[i];
                    System.out.println("Page Faults: " + pagefault);
                }
            }
        }
    }
}
