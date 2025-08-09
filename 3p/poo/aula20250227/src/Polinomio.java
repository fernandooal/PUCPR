import java.util.Scanner;

public class Polinomio {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o valor do coeficiente 'a': ");
        int a = sc.nextInt();

        System.out.print("Digite o valor do coeficiente 'b': ");
        int b = sc.nextInt();

        System.out.print("Digite o valor do coeficiente 'c': ");
        int c = sc.nextInt();

        System.out.print("Digite o valor de 'x': ");
        double x = sc.nextDouble();

        double y = (a*(Math.pow(x, 2)) + (b*x) + c);
        System.out.println("Resultado do cálculo do polinômio: ");
        System.out.println(y);
    }
}
