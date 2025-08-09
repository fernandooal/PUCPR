public class Profissional extends Jogador{
    private double capital;

    public Profissional(String nome, int score, double capital) {
        super(nome, score);
        this.capital = capital;
    }

    public void imprimir() {
        super.imprimir();
        System.out.println("    Profissional: ");
        System.out.println("        Capital: " + capital);
    }

    public void ganhar(int p){
        super.ganhar(p);
        capital += p*4;
    }

    public void perder(int p){
        super.perder(p);
        capital -= p*4;
    }
}
