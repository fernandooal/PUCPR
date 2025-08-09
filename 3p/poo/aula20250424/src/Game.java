import java.util.ArrayList;
import java.util.Scanner;

public class Game {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        ArrayList<Jogador> jogadores = new ArrayList<>();

        setup(jogadores);

        int option = -1;
        while (option != 0) {
            System.out.println("Escolha uma opção: ");
            System.out.println("1 - Criar Principiante");
            System.out.println("2 - Criar Profissional");
            System.out.println("3 - Criar Senior");
            System.out.println("4 - Aplicar método Ganhar em um jogador");
            System.out.println("5 - Aplicar método Perder em um jogador");
            System.out.println("6 - Imprimir um jogador");
            System.out.println("7 - Imprimir todos os jogadores");
            System.out.println("0 - Sair");
            option = sc.nextInt();

            switch (option) {
                case 1: criarPrincipiante(jogadores); break;
                case 2: criarProfissional(jogadores); break;
                case 3: criarSenior(jogadores); break;
                case 4: ganharJogador(jogadores); break;
                case 5: perderJogador(jogadores); break;
                case 6: imprimirJogador(jogadores); break;
                case 7: imprimirTodosJogadores(jogadores); break;
                case 0: break;
                default: System.out.println("Opção inválida!");break;
            }
        }

        System.out.println("Até a próxima! =)");
    }

    private static void setup(ArrayList<Jogador> jogadores) {
        jogadores.add(new Principiante("testePri1", 50, 25));
        jogadores.add(new Principiante("testePri2", 50, 25));
        jogadores.add(new Principiante("testePri3", 50, 25));

        jogadores.add(new Profissional("testePro1", 50, 25));
        jogadores.add(new Profissional("testePro2", 50, 25));
        jogadores.add(new Profissional("testePro3", 50, 25));

        jogadores.add(new Senior("testeS1", 50, 30, 40));
        jogadores.add(new Senior("testeS2", 50, 30, 40));
        jogadores.add(new Senior("testeS3", 50, 30, 40));
    }

    private static void criarPrincipiante(ArrayList<Jogador> jogadores) {
        System.out.println("Digite o nome do principiante: ");
        String nome = sc.next();
        System.out.println("Digite o score do principiante: ");
        int score = sc.nextInt();
        System.out.println("Digite o bônus do principiante: ");
        double bonus = sc.nextInt();

        jogadores.add(new Principiante(nome, score, bonus));
    }

    private static void criarProfissional(ArrayList<Jogador> jogadores) {
        System.out.println("Digite o nome do profissional: ");
        String nome = sc.next();
        System.out.println("Digite o score do profissional: ");
        int score = sc.nextInt();
        System.out.println("Digite o capital do profissional: ");
        double capital = sc.nextDouble();

        jogadores.add(new Profissional(nome, score, capital));
    }

    private static void criarSenior(ArrayList<Jogador> jogadores) {
        System.out.println("Digite o nome do senior: ");
        String nome = sc.next();
        System.out.println("Digite o score do senior: ");
        int score = sc.nextInt();
        System.out.println("Digite o capital do senior: ");
        double capital = sc.nextDouble();
        System.out.println("Digite o prêmio do senior: ");
        double premio = sc.nextDouble();

        jogadores.add(new Senior(nome, score, capital, premio));
    }

    private static void ganharJogador(ArrayList<Jogador> jogadores) {
        System.out.println("Digite o nome do jogador: ");
        String nome = sc.next();
        System.out.println("Digite os pontos que o jogador vai ganhar: ");
        int pontos = sc.nextInt();

        for(Jogador j: jogadores){
            if(j.getNome().equalsIgnoreCase(nome)){
                j.ganhar(pontos);
            }
        }
    }

    private static void perderJogador(ArrayList<Jogador> jogadores) {
        System.out.println("Digite o nome do jogador: ");
        String nome = sc.next();
        System.out.println("Digite os pontos que o jogador vai perder: ");
        int pontos = sc.nextInt();

        for(Jogador j: jogadores){
            if(j.getNome().equalsIgnoreCase(nome)){
                j.perder(pontos);
            }
        }
    }

    private static void imprimirJogador(ArrayList<Jogador> jogadores) {
        System.out.println("Digite o nome do jogador: ");
        String nome = sc.next();

        for (Jogador j : jogadores) {
            if (j.getNome().equalsIgnoreCase(nome)) {
                j.imprimir();
                break;
            }
        }
        System.out.println("=========\n");
    }

    private static void imprimirTodosJogadores(ArrayList<Jogador> jogadores){
        for (Jogador j : jogadores) {
            j.imprimir();
        }
        System.out.println("=========\n");
    }
}
