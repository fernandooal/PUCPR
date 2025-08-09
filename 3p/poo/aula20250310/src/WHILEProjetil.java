import java.util.Scanner;

public class WHILEProjetil {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o angulo: ");
        double angulo = input.nextDouble();
        System.out.println("digite a distancia: ");
        double r = input.nextDouble();
        double g = 9.8;
        angulo = Math.toRadians(angulo);

        double velocidadeInicial = Math.sqrt((r*g)/(2*Math.sin(angulo)*Math.cos(angulo)));
        double tempoLancamento = (2*velocidadeInicial*Math.sin((angulo)))/g;

        double t = 0.0;
        while(t <= tempoLancamento){
            double x = (velocidadeInicial*Math.cos(angulo))*t;
            double y = (velocidadeInicial*Math.sin(angulo))*t - ((g*Math.pow(t,2))/2);

            System.out.printf("t: %.1f - (%.5f,%.5f)%n", t, x, y);
            t += 0.1;
        }
    }
}
