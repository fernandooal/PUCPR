import java.util.Scanner;

public class Ex2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite a temperatura em Celsius: ");
        double celsius = input.nextDouble();

        double fahrenheit = ((9 * celsius) + 160)/5;

        System.out.println("Temperatura em Fahrenheit: " + fahrenheit);
    }
}
