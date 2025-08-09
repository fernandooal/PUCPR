import java.util.Scanner;

public class FORSomatoria {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        double pi = 3.14;
        double z = 0;

        System.out.println("Digite n: ");
        int n  = input.nextInt();

        for(int i = 1; i <= n; i++){
            System.out.println("Digite X: ");
            double x =  input.nextDouble();

            double t = (Math.pow((pi - x), 2)) / i;
            z += t;
        }

        System.out.println(z);
    }
}
