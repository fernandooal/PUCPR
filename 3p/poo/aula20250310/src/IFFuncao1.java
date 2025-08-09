import java.util.Scanner;

public class IFFuncao1 {
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o valor x: ");
        double x = input.nextDouble();

        if(x == 0){
            System.out.println("o valor não pode ser 0");
        } else{
            if(x == 4){
                System.out.println("O valor não pode ser 4");
            } else{
                double y = Math.sqrt(x) / (x-4);
                System.out.println(y);
            }
        }
    }
}
