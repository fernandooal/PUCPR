public class SWITCHCores {
    public static void main(String[] args) {
        int random = (int) (Math.random() * 9);

        switch (random) {
            case 0:
            case 1:
            case 2:
                System.out.println("azul");
                break;
            case 5:
            case 7:
            case 9:
                System.out.println("marrom");
                break;
            default:
                System.out.println("amarelo");
        }

        System.out.println("numero: " + random);
    }
}
