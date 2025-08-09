import java.util.List;

public class Produtos {
    private String nome;
    private double preco;

    public Produtos(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public double getPreco() {
        return preco;
    }

    public static void listProdutos(List<Produtos> produtos){
        for(int i = 0; i < produtos.size(); i++){
            System.out.println((i+1) + " - " + produtos.get(i).nome + " - R$" + String.format("%.2f", produtos.get(i).preco));
        }
    }
}
