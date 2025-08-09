import java.util.Scanner;

public class SWITCHOperacoes {
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o primeiro operando: ");
        double x = input.nextDouble();
        System.out.println("Digite o segundo operando: ");
        double y = input.nextDouble();

        System.out.println("Operações disponíveis: ");
        System.out.println("1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão");
        System.out.println("Digite a sua escolha: ");
        int op = input.nextInt();

        switch(op){
            case 1:
                System.out.println("Resultado:" + (x+y));
                break;
            case 2:
                System.out.println("Resultado:" + (x-y));
                break;
            case 3:
                System.out.println("Resultado:" + (x*y));
                break;
            case 4:
                System.out.println("Resultado:" + (x/y));
                break;
            default:
                System.out.println("Opção invalida");
        }
    }
}
