package Lesson_2;

public class Main {
    public static void main(String[] args) {
        
    


    Market market = new Market();

    Human Jardin = new Human("Jardin");
    Human Jasmin = new Human("Jasmin");

    market.acceptToMarket(Jasmin);
    market.acceptToMarket(Jardin);
    market.update();
    
}
}
