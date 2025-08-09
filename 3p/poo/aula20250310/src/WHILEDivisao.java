import java.util.Scanner;

public class WHILEDivisao {
    public static void  main(String[]args){
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o valor de x: ");
        int x = input.nextInt();

        System.out.println("Digite o valor de y: ");
        int y = input.nextInt();

        int q = 0;
        int r = x;
        while(r >= y){
            r = r - y;
            q++;
        }

        System.out.println("Quociente: " + q);
        System.out.println("Resto: " + r);
    }
}
