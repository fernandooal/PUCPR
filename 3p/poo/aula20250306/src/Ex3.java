import java.util.Scanner;

public class Ex3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o raio da lata: ");
        double raio = input.nextDouble();
        System.out.println("Digite a altura da lata: ");
        double altura = input.nextDouble();

        double volume = 3.14159 * (Math.pow(raio, 2)) * altura;

        System.out.println("Volume: " + volume);
    }
}
