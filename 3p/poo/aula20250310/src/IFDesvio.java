import java.util.Scanner;

public class IFDesvio {
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

        double media = (x1+x2+x3+x4+x5)/n;

        double soma = 0;
        soma += Math.pow((x1 - media), 2);
        soma += Math.pow((x2 - media), 2);
        soma += Math.pow((x3 - media), 2);
        soma += Math.pow((x4 - media), 2);
        soma += Math.pow((x5 - media), 2);

        double dp = Math.sqrt(soma/n);
        System.out.println("Resultado do cálculo do desvio padrão: ");
        System.out.println(dp);

    }
}
