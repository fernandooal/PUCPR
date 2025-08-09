public class Principiante extends Jogador {
    private Double bonus;

    public Principiante(String nome, int score, double bonus) {
        super(nome, score);
        this.bonus = bonus;
    }

    public void imprimir() {
        super.imprimir();
        System.out.println("    Principiante: ");
        System.out.println("        Bônus: " + bonus);
    }

    public void ganhar(int p){
        super.ganhar(p);
        bonus += p*0.1;
    }

    public void perder(int p){
        super.perder(p);
        bonus -= p*0.1;
    }
}
