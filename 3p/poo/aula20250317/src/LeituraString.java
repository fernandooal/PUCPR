import java.util.Scanner;
public class LeituraString {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        String frase = teclado.nextLine();
        System.out.println(frase);
        String palavra = teclado.next();
        System.out.println(palavra);
    }
}