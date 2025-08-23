import myutils.ArrayList;

public class TestesArray {
    public static void main(String[] args) {

        ArrayList<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);
        list.add(6);
        list.add(7);
        list.add(8);
        list.add(9);
        list.add(10);
        System.out.println(list);

        list.add(2,10);
        System.out.println(list);
        list.remove(2);
        System.out.println(list);
        list.remove(new Integer(4));
        System.out.println(list);
        list.set(1, 10);
        System.out.println(list.get(1));
        System.out.println(list.contains(new Integer(88)));
        System.out.println(list.indexOf(new Integer(5)));
    }
}
