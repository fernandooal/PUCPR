import java.util.Scanner;

public class MembrosEstaticos {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Escolha uma operação: ");
        System.out.println("1. Converter string em maiúscula;");
        System.out.println("2. Converter string em minúscula;");
        System.out.println("3. Extrair substring");
        System.out.println("4. Localizar substring");
        System.out.println("5. Comparar duas strings");
        System.out.println("0. Sair");
        int op = sc.nextInt();
        sc.nextLine();

        String string = "";
        if (op != 0) {
            System.out.print("Digite uma string: ");
            string = sc.nextLine();
        }

        switch (op) {
            case 1:
                String resultado1 = MembrosOperacoes.converter_maiusculo(string);
                System.out.println(resultado1);
                break;
            case 2:
                String resultado2 = MembrosOperacoes.converter_minusculo(string);
                System.out.println(resultado2);
                break;
            case 3:
                System.out.print("Digite o range 1: ");
                int range1 = sc.nextInt();
                System.out.print("Digite o range 2: ");
                int range2 = sc.nextInt();
                String resultado3 = MembrosOperacoes.extrair_substring(string, range1, range2);
                System.out.println(resultado3);
                break;
            case 4:
                System.out.print("Digite a substring: ");
                String substring = sc.nextLine();
                int resultado4 = MembrosOperacoes.localizar_substring(string, substring);
                System.out.println(resultado4);
                break;
            case 5:
                System.out.print("Digite a segunda string: ");
                String string2 = sc.nextLine();
                boolean resultado5 = MembrosOperacoes.comparar_strings(string, string2);
                System.out.println(resultado5 ? "São iguais!" : "São diferentes!");
                break;
            case 0:
                System.out.println("Saindo...");
                break;
            default:
                System.out.println("Opção inválida!");
        }
    }
}
