import java.util.Scanner;

public class FORFatorial {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o número para calcular o fatorial: ");
        int n = input.nextInt();

        int f;
        for(f = 1; n > 1; n--){
            f = f * n;
        }

        System.out.println("Fatorial: " + f);
    }
}
