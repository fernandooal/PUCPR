import java.util.Scanner;

public class Ex1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o valor da sua hora aula: ");
        double horaAula = input.nextDouble();
        System.out.println("Digite o número de aulas dadas no mês: ");
        int aulas = input.nextInt();
        System.out.println("Digite o percentual de desconto do INSS: ");
        double inss =  input.nextDouble();
        System.out.println("Digite o percentual de desconto do IR: ");
        double ir = input.nextDouble();

        double total = horaAula * aulas;
        double descontoInss = (total*(inss/100));
        double descontoIR = (total*(ir/100));

        System.out.println("O seu salário líquido é: " + (total-descontoInss-descontoIR));
    }
}
