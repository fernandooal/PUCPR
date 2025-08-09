import java.util.Scanner;

public class IFMenor {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Escreva 3 números: ");
        double a = input.nextDouble();
        double b  = input.nextDouble();
        double c = input.nextDouble();

        double menor;
        if(a<b && a<c){
            menor = a;
            System.out.println("o primeiro é o menor: ");
        } else{
            if(b < a && b < c){
                menor = b;
                System.out.println("O segundo é o menor: ");
            } else{
                menor = c;
                System.out.println("O terceiro é o menor: ");
            }
        }
        System.out.println(menor);
    }
}
