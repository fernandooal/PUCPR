import java.util.Scanner;

public class FORMedia {
    public static void main(String[]args){
        Scanner input = new Scanner(System.in);

        double soma = 0;
        for(int i = 0; i < 20; i++){
            System.out.println("Digite uma nota: ");
            soma += input.nextDouble();
        }

        double media = soma/20;
        System.out.println("média: "+media);
    }
}
