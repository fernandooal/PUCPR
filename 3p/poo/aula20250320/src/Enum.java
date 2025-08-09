public class Enum {
    public static void main(String[] args) {
        enum Dia_da_Semana {
            SEGUNDA, TERCA, QUARTA, QUINTA, SEXTA, SABADO, DOMINGO
        }
        Dia_da_Semana dia = Dia_da_Semana.SEGUNDA;
        if (dia == Dia_da_Semana.DOMINGO)
            System.out.println("Take a break!");
        else
            System.out.println("Do your homework!");
        String day_of_week = null;
        switch (dia)
        {
            case SEGUNDA: day_of_week = "Monday"; break;
            case TERCA: day_of_week = "Tuesday"; break;
            case QUARTA: day_of_week = "Wednesday"; break;
            case QUINTA: day_of_week = "Thursday"; break;
            case SEXTA: day_of_week = "Friday"; break;
            case SABADO: day_of_week = "Saturday"; break;
            case DOMINGO: day_of_week = "Sunday";
        }
        System.out.println("Day of week: " + day_of_week);
    }
}