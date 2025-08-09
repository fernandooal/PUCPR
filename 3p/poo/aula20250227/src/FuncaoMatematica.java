import java.util.Scanner;

public class FuncaoMatematica {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite um numero 'x': ");
        double x = sc.nextDouble();

        if(x <= 0){
            System.out.println("O número 'x' não pode ser menor ou igual a 0.");
        } else{
            if(x == 4){
                System.out.println("O número 'x' não pode ser igual a 4.");
            } else{
                double y = Math.sqrt(x) / (x - 4);
                System.out.println("Y: " + y);
            }
        }
    }
}
