import java.util.Scanner;

public class IFFuncao {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o valor de x: ");
        double x = input.nextDouble();

        if(x <= 4){
            System.out.println("O valor de X não pode ser menor ou igual a 4");
        } else{
            double y = Math.sin(Math.toRadians(x)) / Math.sqrt(x);

            System.out.println(y);
        }
    }
}
