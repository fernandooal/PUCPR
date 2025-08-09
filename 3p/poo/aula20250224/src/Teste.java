import java.util.Scanner;

class Teste {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nome = teclado.next();

        System.out.print("Digite sua idade: ");
        int idade = teclado.nextInt();

        System.out.println("Olá " + nome + ", você tem " + idade + " anos!");
    }
}