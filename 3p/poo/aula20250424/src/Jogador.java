public class Jogador {
    private String nome;
    protected int score;

    public Jogador(String nome, int score) {
        this.nome = nome;
        this.score = score;
    }

    public void imprimir() {
        System.out.println("=========");
        System.out.println("Jogador:");
        System.out.println("Nome: " + nome);
        System.out.println("Score: " + score);
    }

    public String getNome() {
        return nome;
    }

    public void ganhar(int p) {
        score += p;
    }

    public void perder(int p) {
        score -= p;
    }
}
