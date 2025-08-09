import java.util.Scanner;

public class Circulo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o valor do raio: ");
        double raio = sc.nextDouble();

        double area = Math.PI * Math.pow(raio, 2);
        double perimetro =  2 * Math.PI * raio;

        System.out.println("Área do círculo: " + String.format("%.2f", area));
        System.out.println("Perímetro do círculo: " + String.format("%.2f", perimetro));
    }
}
