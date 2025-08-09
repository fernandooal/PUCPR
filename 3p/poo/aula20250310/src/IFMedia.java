import java.util.Scanner;

public class IFMedia {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o tamanho da amostra: ");
        int n = input.nextInt();

        System.out.println("Digite o valor 1: ");
        double x1 = input.nextDouble();
        System.out.println("Digite o valor 2: ");
        double x2 = input.nextDouble();
        System.out.println("Digite o valor 3: ");
        double x3 = input.nextDouble();

        double x4 = 0;
        double x5 = 0;

        if(n > 3){
            System.out.println("Digite o valor 4: ");
            x4 = input.nextDouble();

            if(n > 4){
                System.out.println("Digite o valor 5: ");
                x5 = input.nextDouble();
            }
        }

        double media = (x1+x2+x3+x4+x5) / n;
        System.out.println("Resultado da média aritmética: " + media);
    }
}
