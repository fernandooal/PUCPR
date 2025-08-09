import java.time.LocalDate;
import java.util.Scanner;

public class Ex4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o horário no formato hhmm: ");
        int horario = input.nextInt();

        int horas = horario / 100;
        int minutos = horario % 100;

        int totalMinutos = (horas*60)+minutos;
        System.out.println("Total: "+totalMinutos);
    }
}
