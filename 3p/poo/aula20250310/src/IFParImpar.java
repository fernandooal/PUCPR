import java.util.Scanner;

public class IFParImpar {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite um número inteiro: ");
        int n =  input.nextInt();

        if(n%2==0)
            System.out.println("Par");
        else
            System.out.println("Impar");
    }
}
