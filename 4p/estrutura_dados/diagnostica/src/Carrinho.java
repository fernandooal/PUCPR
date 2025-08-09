import java.util.ArrayList;
import java.util.List;

public class Carrinho {
    String nome;
    List<Produtos> produtos;

    public Carrinho(String nome) {
        this.nome = nome;
        this.produtos = new ArrayList<>();
    }

    public List<Produtos> getProdutos(){
        return produtos;
    }

    public void addProduto(Produtos produto) {
        produtos.add(produto);
    }

    public double calcularTotal(double taxa) {
        double total = 0;

        for(Produtos p : produtos){
            total += p.getPreco() * (1+taxa);
        }

        return total;
    }
}
