import myutils.Pilha;

public class TestesPilha {
    public static void main(String[] args) {
        Pilha<Integer> pilha = new Pilha<>();

        pilha.push(1);
        pilha.push(2);
        pilha.push(3);

        pilha.print();

        System.out.println(pilha.isEmpty());

        System.out.println(pilha.pop());
        System.out.println(pilha.pop());
        System.out.println(pilha.pop());

        System.out.println(pilha.isEmpty());

        pilha.push(1);
        pilha.push(2);
        pilha.push(3);

        pilha.print();

        pilha.clear();
        pilha.print();
        System.out.println(pilha.isEmpty());
    }
}
