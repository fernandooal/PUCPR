import java.util.Scanner;

public class Ex5 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o tempo gasto na viagem (em horas): ");
        int tempo = input.nextInt();
        System.out.println("Digite a velocidade média (em km/h): ");
        double velocidade = input.nextDouble();

        double distancia =  tempo * velocidade;

        double volume = distancia / 12;

        System.out.println("Volume de combustível gasto: " + volume);
    }
}
