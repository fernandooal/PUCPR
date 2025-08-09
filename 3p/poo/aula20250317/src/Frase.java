public class Frase {
    public static void main(String[] args) {
//        String frase = new String(" Mas eis que chega a roda-viva ");
//        System.out.println(frase);
//        System.out.println("|" + frase + "|");
//        String frase_limpa = frase.trim();
//        System.out.println("|" + frase_limpa + "|");
//        frase = frase_limpa;

        String s1 = new String("Pimenta");
        String s2 = new String("Rosa");
        String s3 = s1 + s2;
        System.out.println(s3);
        String s4 = s1.concat(s2);
        System.out.println(s4);
        String s5 = s1 + " " + s2;
        System.out.println(s5);
        String s6 = s5 + 10;
        System.out.println(s6);
        String s7 = s5 + 10 + 20;
        System.out.println(s7);
        String s8 = s5 + (10 + 20);
        System.out.println(s8);
    }
}