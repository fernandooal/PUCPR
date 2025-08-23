import myutils.Fila;

public class TestesFila {
    public static void main(String[] args) {
        Fila<Integer> fila = new Fila<Integer>();

        fila.enqueue(1);
        fila.enqueue(2);
        fila.enqueue(3);

        fila.print();

        System.out.println(fila.isEmpty());

        System.out.println(fila.dequeue());
        System.out.println(fila.dequeue());
        System.out.println(fila.dequeue());

        System.out.println(fila.isEmpty());

        fila.enqueue(1);
        fila.enqueue(2);
        fila.enqueue(3);

        fila.print();
        fila.clear();
        fila.print();

        System.out.println(fila.isEmpty());
    }
}
