import java.util.Scanner;

public class Ex6 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Digite o número da placa do veículo: ");
        int placa = input.nextInt();

        int estado = placa / 1000;
        int cidade = (placa-(estado*1000))/100;
        int veiculo = placa % 100;

        System.out.println("Estado: "+estado);
        System.out.println("Cidade: "+cidade);
        System.out.println("Veiculo: "+veiculo);
    }
}
