import java.util.Scanner;

public class WHILEIntegral {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite a: ");
        double a  = input.nextDouble();
        System.out.println("Digite b: ");
        double b = input.nextDouble();

        if(a <= b){
            System.out.println("Digite n: ");
            int n = input.nextInt();

            if(n > 0){
                double area_total = 0;
                double x = a;
                double h = (b-a) / n;
                double y1 = 2*(Math.sin(x)) + (Math.cos(x)/3);
                int i = 0;

                while(i < n){
                    x += h;
                    double y2 = 2*(Math.sin(x)) + (Math.cos(x)/3);
                    double area_trapezio = ((y1 + y2) / 2) * h;
                    area_total += area_trapezio;
                    y1 = y2;
                    i++;
                }
                System.out.println(area_total);
            } else{
                System.out.println("Erro: o valor de n deve ser maior que zero");
            }
        } else{
            System.out.println("Erro: valor de a deve ser menor ou igual ao valor de b");
        }
    }
}
