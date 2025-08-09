public class Camiseta {
    private String marca;
    private Modelo modelo;
    private Tamanho tamanho;
    private Cor cor;
    private double preco;
    private int estoque;

    public enum Modelo { TRADICIONAL, REGATA, GOLA_V }
    public enum Tamanho { PEQUENO, MEDIO, GRANDE, EXTRA_GRANDE }
    public enum Cor { BRANCA, PRETA, AZUL, AMARELA }

    public Camiseta(String marca, Modelo modelo, Tamanho tamanho, Cor cor, double preco, int estoque){
        this.marca = marca;
        this.modelo = modelo;
        this.tamanho = tamanho;
        this.cor = cor;
        this.preco = preco;
        this.estoque = estoque;
    }

    public void exibirAtributos(){
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Tamanho: " + tamanho);
        System.out.println("Cor: " + cor);
        System.out.println("Preco: R$" + preco);
        System.out.println("Estoque: " + estoque);
    }
}
