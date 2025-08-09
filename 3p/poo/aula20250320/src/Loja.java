public class Loja {
    public static void main(String[] args) {
        Camiseta[] camisas = new Camiseta[4];

        camisas[0] = new Camiseta("Nike", Camiseta.Modelo.TRADICIONAL, Camiseta.Tamanho.MEDIO, Camiseta.Cor.BRANCA, 99.90, 10);
        camisas[1] = new Camiseta("Adidas", Camiseta.Modelo.REGATA, Camiseta.Tamanho.GRANDE, Camiseta.Cor.PRETA, 89.90, 15);
        camisas[2] = new Camiseta("Puma", Camiseta.Modelo.GOLA_V, Camiseta.Tamanho.PEQUENO, Camiseta.Cor.AZUL, 79.90, 5);
        camisas[3] = new Camiseta("Reebok", Camiseta.Modelo.TRADICIONAL, Camiseta.Tamanho.EXTRA_GRANDE, Camiseta.Cor.AMARELA, 109.90, 8);

        for(int i = 0; i < 4; i++){
            System.out.println("---------------");
            camisas[i].exibirAtributos();
        }
    }
}
