import java.util.Scanner;

public class IFEquacao {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("digite o coeficiente a:");
        double a = input.nextDouble();
        System.out.println("digite o coeficiente b:");
        double b = input.nextDouble();
        System.out.println("digite o coeficiente c:");
        double c = input.nextDouble();

        double delta = (b*b) - (4*a*c);
        if(delta<0){
            System.out.println("não existe raiz real");
        } else{
            if(delta==0){
                System.out.println("Existe apenas uma raiz real:");
                double x1 = -b / (2*a);
                System.out.println(x1);
            } else{
                System.out.println("Existem duas raizes reais:");
                double x1 = (-b + Math.sqrt(delta))/(2*a);
                double x2 = (-b - Math.sqrt(delta))/(2*a);
                System.out.println(x1);
                System.out.println(x2);
            }
        }
    }
}
