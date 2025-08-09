import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Restaurante {

    static Scanner input = new Scanner(System.in);
    public static void main(String[] args){
        int opcao = 1;

        while(opcao != 0){
            menu();

            try{
                opcao = input.nextInt();
                if(opcao < 0 || opcao > 1){
                    System.out.println("Escolha uma opção dentre as fornecidas!");
                }
            } catch (Exception e) {
                System.out.println("Digite um número inteiro válido!");
                input.nextLine();
                opcao = 1;
            }

            if(opcao == 1){
                pedido();
            }
        }

        System.out.println("Volte sempre =)");

    }

    private static void menu(){
        System.out.println("Restaurante Estrutura de Dados!");
        System.out.println("0 - Sair");
        System.out.println("1 - Fazer Pedido");
    }

    private static void pedido(){
        System.out.println("Digite o seu nome: ");
        input.nextLine();
        String nome = input.nextLine();
        List<Produtos> produtos = new ArrayList<>();
        Carrinho carrinho = new Carrinho(nome);
        double taxa = 0.1;

        produtos.add(new Produtos("Hamburguer", 30));
        produtos.add(new Produtos("Batata Frita", 15));
        produtos.add(new Produtos("Prato Feito", 20));
        produtos.add(new Produtos("Coca-Cola", 6));
        produtos.add(new Produtos("Pepsi", 5));

        System.out.println("====Cardápio do Restaurante====\n");
        System.out.println("0 - Finalizar Pedido");
        Produtos.listProdutos(produtos);

        int opcao = 1;
        while(opcao != 0){
            System.out.println("Digite o número do produto para adicionar ao carrinho: ");
            try{
                opcao = input.nextInt();
                if(opcao < 0 || opcao > 5){
                    System.out.println("Escolha uma opção dentre as fornecidas!");
                }
            } catch (Exception e) {
                System.out.println("Digite um número inteiro válido!");
                input.nextLine();
                opcao = 1;
            }

            if(opcao != 0){
                carrinho.addProduto(produtos.get(opcao-1));
            }
        }

        pagamento(carrinho, taxa);
    }

    private static void pagamento(Carrinho carrinho, double taxa){
        double valorTotal = carrinho.calcularTotal(taxa);

        System.out.println("\n===Nota Fiscal===");
        Produtos.listProdutos(carrinho.getProdutos());
        System.out.println("\nTaxa de serviço: "+ taxa*100 + "%");
        System.out.println("\nValor total: R$"+ String.format("%.2f", valorTotal));

        double valorRecebido = 0;
        boolean valido = false;
        while (!valido) {
            System.out.print("\nDigite o valor que foi recebido em dinheiro: ");

            try{
                valorRecebido = input.nextDouble();
                if (valorRecebido < valorTotal){
                    System.out.println("Valor insuficiente!");
                } else{
                    valido = true;
                }
            } catch (Exception e) {
                System.out.println("Valor inválido! Digite um número decimal.");
                input.nextLine();
            }
        }

        double troco = valorRecebido - valorTotal;
        System.out.println("\n===Troco: R$"+ String.format("%.2f",troco) + "===\n");
    }
}
