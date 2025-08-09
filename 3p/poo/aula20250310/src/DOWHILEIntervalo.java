import java.util.Scanner;

public class DOWHILEIntervalo {
    public static void main (String[]args){
        Scanner input = new Scanner(System.in);

        int n = 0;

        //versao 1 - tentativas ilimitadas
//        do{
//            System.out.println("Digite o valor de n: ");
//            n = input.nextInt();
//        } while(n < 5 || n > 10);

        //versao 2 - 5 tentativas
        int tentativas = 5;
        do{
            System.out.println("Digite o valor de n: ");
            n = input.nextInt();
            tentativas--;
        } while((n < 5 || n > 10) && tentativas > 0);

        if(tentativas == 0 && (n < 5 || n > 10)){
            System.out.println("Limite de tentativas atingido");
        } else{
            System.out.println(n);
        }
    }
}
