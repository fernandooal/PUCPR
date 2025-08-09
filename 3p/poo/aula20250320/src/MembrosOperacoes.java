public class MembrosOperacoes {
    public static String converter_maiusculo(String string){
        return string.toUpperCase();
    }

    public static String converter_minusculo(String string){
        return string.toLowerCase();
    }

    public static String extrair_substring(String string, int range1, int range2){
        return string.substring(range1, range2);
    }

    public static int localizar_substring(String string, String substring){
        return string.indexOf(substring);
    }

    public static boolean comparar_strings(String string1, String string2){
        return string1.compareToIgnoreCase(string2) == 0;
    }
}
