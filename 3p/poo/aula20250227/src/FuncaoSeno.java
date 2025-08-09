import java.util.Scanner;

public class FuncaoSeno {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o valor de x: ");
        double x =  sc.nextDouble();

        if(x <= 4){
            System.out.print("O valor de 'x' não pode ser menor ou igual a 4");
        } else{
            double y = Math.sin(x) / Math.sqrt(x-4);
            System.out.println("Y (em radianos): " + y);
        }
    }
}
