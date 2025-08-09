import java.util.Scanner;

public class OrdemLexicografica {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Digite a string 1: ");
        String string1 = input.nextLine();
        System.out.print("Digite a string 2: ");
        String string2 = input.nextLine();
        System.out.print("Digite a string 3: ");
        String string3 = input.nextLine();

        System.out.println("Ordem Lexicografica: ");
        if(string1.compareToIgnoreCase(string2) >= 0 && string1.compareToIgnoreCase(string3) <= 0){
            System.out.println(string1);

            if(string2.compareToIgnoreCase(string3) >= 0){
                System.out.println(string2);
                System.out.println(string3);
            } else{
                System.out.println(string3);
                System.out.println(string2);
            }
        } else if (string2.compareToIgnoreCase(string1) >= 0 && string2.compareToIgnoreCase(string3) <= 0){
            System.out.println(string2);

            if(string1.compareToIgnoreCase(string3) >= 0){
                System.out.println(string1);
                System.out.println(string3);
            } else{
                System.out.println(string3);
                System.out.println(string1);
            }
        } else{
            System.out.println(string3);

            if(string1.compareToIgnoreCase(string2) >= 0){
                System.out.println(string1);
                System.out.println(string2);
            } else{
                System.out.println(string2);
                System.out.println(string1);
            }
        }
    }
}
